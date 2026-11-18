---
layout: default
title: Blog
---

<section class="featured-posts">
  {% for post in site.posts limit:5 %}
    <article class="full-post">
      <div class="post-content">
        <h2 class="article-title">
          <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        </h2>
        
        <p class="post-meta">
          <a href="{{ post.url | relative_url }}"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %-d, %Y" }} &middot; {{ post.date | date: "%A" }}</time></a>
        </p>

        {{ post.content }}
      </div>
    </article>
    {% unless forloop.last %}<hr class="post-divider" />{% endunless %}
  {% endfor %}
</section>

{% if site.posts.size > 5 %}
<section class="archive-posts">
  <h3>Older Posts</h3>
  <ul class="archive-list">
    {% for post in site.posts offset:5 limit:5 %}
      <li class="archive-item">
        <div class="archive-main">
          <a href="{{ post.url | relative_url }}" class="archive-title">{{ post.title }}</a>
        </div>
        <time class="archive-date" datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %d, %Y" }}</time>
      </li>
    {% endfor %}
  </ul>
</section>
{% endif %}

<div class="blog-archive-link">
  <a href="{{ '/blog/' | relative_url }}{% if site.posts.size > 10 %}#more-posts{% endif %}">View all posts in Blog Archive</a>
</div>
