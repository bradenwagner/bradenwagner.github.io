---
layout: archive
title: "Sitemap"
permalink: /sitemap/
author_profile: true
---

{% include base_path %}

A list of all pages on this site.

{% assign titled_pages = site.pages | where_exp: "item", "item.title" %}
{% for post in titled_pages %}
  {% include archive-single.html %}
{% endfor %}
