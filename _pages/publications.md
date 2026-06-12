---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

<div class="publications-page" markdown="1">

This page collects my research papers and preprints.

{% if site.author.googlescholar %}
  <p class="publications-page__note">You can also find my articles on <a href="{{ site.author.googlescholar }}">my Google Scholar profile</a>.</p>
{% endif %}

{% include base_path %}

<div class="publication-list">
{% for post in site.publications reversed %}
  {% include publication-single.html %}
{% endfor %}
</div>

</div>
