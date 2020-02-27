---
permalink: /news
---

# News

Want to keep up with the AIP system, and what we are working on? Welcome to the
**AIP newsletter**, a monthly publication covering new AIP guidance, and any
other developments useful to API producers.

<!-- prettier-ignore -->
{% assign rev_pages = site.pages | reverse -%}
{% for p in rev_pages %}{% if p.newsletter -%}

### {{ p.newsletter.month }} {{ p.newsletter.year }}

##### [**{{ p.title }}**]({{ p.permalink }})

{{ p.newsletter.description }}

{% if p.newsletter.aips.reviewing or p.newsletter.other %}

<div class="aip-newsletter-highlights">
  <p>Highlights:</p>
  <ul class="highlights-list">
    {% if p.newsletter.aips.reviewing %}
    <li class="highlight-item">Reviewing:
      <ul>
        {% for aip in p.newsletter.aips.reviewing %}
        <li><a href="/{{ aip }}">AIP-{{ aip }}</a></li>
        {% endfor %}
      </ul>
    </li>
    {% endif %}
    {% for other in p.newsletter.other %}
    <li>{{ other }}</li>
    {% endfor %}
  </ul>
</div>
{% endif %}

{% endif %}{% endfor -%}

<!-- prettier-ignore-end -->
