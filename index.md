---
layout: default
title: Blog
---

<section class="featured-posts">
  {% for post in site.posts limit:5 %}
    <article class="full-post">
      <h2>
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      </h2>
      
      <p class="post-meta">
        <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time>
      </p>

      <div class="post-content">
        {{ post.content }}
      </div>
    </article>
    <hr class="post-divider" />
  {% endfor %}
</section>

{% if site.posts.size > 5 %}
<section class="archive-posts">
  <h3>Older Posts</h3>
  <ul class="compact-post-list">
    {% for post in site.posts offset:5 %}
      <li>
        <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%Y-%m-%d" }}</time>
        — 
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      </li>
    {% endfor %}
  </ul>
</section>
{% endif %}

<!-- Link to full Blog Page -->
<div class="blog-archive-link">
  <a href="{{ '/blog/' | relative_url }}">View all posts in Blog &rarr;</a>
</div>
