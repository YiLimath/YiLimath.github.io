---
layout: archive
title: ""
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<div class="cv-page" markdown="1">

<div class="cv-hero" markdown="1">

Third-year PhD student at Wuhan University, working in birational geometry and moduli theory.

<a class="btn cv-download" href="{{ base_path }}/files/CV.pdf">Download full CV (PDF)</a>

</div>

<section class="cv-section" markdown="1">

## Education

<div class="cv-timeline">
  <div class="cv-timeline__item">
    <div class="cv-timeline__year">2023–present</div>
    <div class="cv-timeline__body">
      <strong>Ph.D. in Birational Geometry</strong><br>
      Wuhan University
    </div>
  </div>
  <div class="cv-timeline__item">
    <div class="cv-timeline__year">2015</div>
    <div class="cv-timeline__body">
      <strong>Bachelor's and Master's degrees in Artificial Intelligence and Automation</strong><br>
      Science and Engineering Interdisciplinary Innovation Experimental Class, Huazhong University of Science and Technology
    </div>
  </div>
</div>

</section>

<section class="cv-section" markdown="1">

## Research Interests

- Kähler minimal model program;
- Structure of Kähler Calabi–Yau varieties and varieties with nef anticanonical divisors;
- Boundedness and moduli aspects of birational geometry.

</section>

<section class="cv-section cv-section--entries" markdown="1">

## Publications

<div class="cv-entry-list">
{% for post in site.publications reversed %}
  {% include archive-single-cv.html %}
{% endfor %}
</div>

</section>

<section class="cv-section cv-section--entries" markdown="1">

## Talks and Travel

<div class="cv-entry-list">
{% for post in site.talks reversed %}
  {% include archive-single-talk-cv.html %}
{% endfor %}
</div>

</section>

<section class="cv-section cv-section--entries" markdown="1">

## Teaching

<div class="cv-entry-list">
{% for post in site.teaching reversed %}
  {% include archive-single-cv.html %}
{% endfor %}
</div>

</section>

<section class="cv-section" markdown="1">

## Honors, Grants and Awards

<div class="cv-timeline">
  <div class="cv-timeline__item">
    <div class="cv-timeline__year">2025</div>
    <div class="cv-timeline__body">Third Prize, Voice of Luojia Teaching Competition, Wuhan University</div>
  </div>
  <div class="cv-timeline__item">
    <div class="cv-timeline__year">2022</div>
    <div class="cv-timeline__body">First Prize in the Qualifying Examination for Riemannian Geometry, Huazhong University of Science and Technology</div>
  </div>
  <div class="cv-timeline__item">
    <div class="cv-timeline__year">2016</div>
    <div class="cv-timeline__body">First Prize, National College Mathematics Competition, Hubei Division</div>
  </div>
</div>

</section>

</div>
