require 'cgi'
require 'time'
require 'date'

module YesterdayReader
  def edition_articles(edition)
    ids = edition['article_ids'] || []
    @context.registers[:site].collections['articles'].docs.select { |a| ids.include?(a.data['article_id']) }
      .sort_by { |a| [a.data['rank'] || 999, a.data['article_id']] }
  end

  def edition_lead(edition)
    articles = edition_articles(edition)
    articles.find { |a| a.data['article_id'] == edition['lead_article_id'] } || articles.first
  end

  def linked_takeaways(edition)
    articles = edition_articles(edition)
    (edition['tldr'] || []).map.with_index do |point, index|
      if point.is_a?(Hash)
        article = articles.find { |a| a.data['article_id'] == point['article_id'] }
        { 'text' => point['text'], 'url' => article&.url }
      else
        { 'text' => point, 'url' => (articles[index] || articles.first)&.url }
      end
    end
  end

  def reading_time(content)
    text = content.to_s.gsub(/\[([^\]]+)\]\([^)]*\)/, '\\1').gsub(/<[^>]*>/, ' ')
    [(text.scan(/[[:alnum:]_]+(?:[’'–-][[:alnum:]_]+)*/u).length / 220.0).ceil, 1].max
  end

  def reader_date(value, pattern = '%B %-d, %Y')
    return '' if value.nil?
    text = value.to_s
    # Jekyll sets TZ from _config.yml before loading plugins (including DST).
    date = text.match?(/T|\d{2}:\d{2}/) ? Time.parse(text).getlocal : Date.parse(text)
    date.strftime(pattern)
  end

  def source_kind_label(kind)
    { 'preprint' => 'Research preprint', 'vendor' => 'Vendor documentation', 'research' => 'Research',
      'reporting' => 'Reporting', 'practitioner' => 'Practitioner perspective' }[kind] || 'Sourced analysis'
  end

  def article_toc(content)
    content.to_s.scan(/<h2\b[^>]*\bid="([^"]+)"[^>]*>(.*?)<\/h2>/m)
      .map { |id, text| { 'id' => id, 'text' => CGI.unescapeHTML(text.gsub(/<[^>]*>/, '')) } }
  end

  def missing_anchors(anchors, content)
    present = content.to_s.scan(/\bid="([^"]+)"/).flatten
    (anchors || []) - present
  end

  def related_articles(article)
    data = article.respond_to?(:data) ? article.data : article
    topics = data['topics'] || []
    @context.registers[:site].collections['articles'].docs.reject { |a| a.data['article_id'] == data['article_id'] }
      .map { |a| [a, (topics & (a.data['topics'] || [])).length] }.select { |pair| pair[1] > 0 }
      .sort_by { |a, score| [-score, -Date.parse(a.data['edition_date'].to_s).jd, a.data['rank'] || 999] }
      .first(3).map(&:first)
  end

  def share_image_for(page)
    site = @context.registers[:site]
    return page['hero'] if page['hero']
    return page['share_image'] if page['share_image'].is_a?(Hash)
    edition = if page['url'] == '/'
      site.collections['editions'].docs.max_by { |e| e.data['edition_date'].to_s }
    elsif page['collection'] == 'editions'
      page
    end
    if edition
      lead = edition_lead(edition)
      return lead.data['hero'] if lead && lead.data['hero']
    end
    site.config['share_image']
  end
end

Liquid::Template.register_filter(YesterdayReader)

module YesterdayTopics
  class TopicPages < Jekyll::Generator
    safe true
    priority :normal

    def generate(site)
      (site.data['topics'] || []).each do |topic|
        next unless site.collections['articles'].docs.any? { |a| (a.data['topics'] || []).include?(topic['slug']) }
        page = Jekyll::PageWithoutAFile.new(site, site.source, "topics/#{topic['slug']}", 'index.html')
        page.data = { 'layout' => 'topic', 'title' => topic['name'], 'description' => topic['description'],
                      'eyebrow' => 'Follow a subject', 'topic_slug' => topic['slug'], 'job' => 'discover' }
        site.pages << page
      end
    end
  end
end
