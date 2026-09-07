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

Final-year PhD candidate at Wuhan University, working in birational geometry.

<a class="btn cv-download" href="{{ base_path }}/files/CV.pdf">Download full CV (PDF)</a>

</div>

<section class="cv-section" markdown="1">

## Education

<div class="cv-timeline">
  <div class="cv-timeline__item">
    <div class="cv-timeline__year">2023–2026</div>
    <div class="cv-timeline__body">
      <strong>Ph.D. in Pure Mathematics</strong><br>
      Wuhan University. Advisors: Sheng Rao and Christopher D. Hacon.<br>
      Expected December 2026.
    </div>
  </div>
  <div class="cv-timeline__item">
    <div class="cv-timeline__year">2019–2022</div>
    <div class="cv-timeline__body">
      <strong>M.Eng. in Artificial Intelligence and Automation</strong><br>
      Huazhong University of Science and Technology
    </div>
  </div>
  <div class="cv-timeline__item">
    <div class="cv-timeline__year">2015–2019</div>
    <div class="cv-timeline__body">
      <strong>B.Eng. in Artificial Intelligence and Automation</strong><br>
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
