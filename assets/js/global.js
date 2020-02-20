// Copyright 2019 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      https://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// This file contains JavaScript-applied rules that can be applied
// to documentation sites using this Jekyll theme generally.
$.when($.ready).then(() => {
  // Make callouts for notes, warnings, etc. work.
  for (let callout of ['Important', 'Note', 'TL;DR', 'Warning']) {
    $(`p strong:contains(${callout}:)`)
      .parent()
      .addClass(callout.replace(';', '').toLowerCase());
  }

  // Make "spec terms" (must, should, may, must not, should not) that
  // are bold-faced be further emphasized.
  for (let directive of ['may', 'must', 'must not', 'should', 'should not']) {
    $('strong')
      .filter((i, el) => $(el).text() === directive)
      .addClass('spec-directive')
      .addClass(`spec-${directive.split(' ')[0]}`);
  }

  // Make AIP banners appear in a better spot.
  $('#aip-state-banner').insertAfter('#aip-main h1');

  // Control the maximum height of the nav sidebar.
  $(window)
    .on('resize', () => {
      $('nav.docs-component-nav').css({
        maxHeight: `${$(window).height() - 110}px`,
      });
    })
    .resize();

  // Intercept level 4 headings in AIPs and make them into responsive tabs.
  $('h2,h3').each((_, section) => {
    // Sanity check: Are we adding tabs to this section at all?
    section = $(section);
    if (section.nextAll('h4').length === 0) {
      return;
    }

    // Set up a placeholder element so we can safely put our tabs back in
    // the right place.
    let anchor = $('<div id="aip-tab-anchor"></div>').insertBefore(
      section.nextAll('h4').eq(0)
    );

    // Group everything that comes after the <h4> into its own content
    // div, according to what Glue expects.
    let secId = section.attr('id');
    let tabs = [];
    $(section)
      .nextUntil('h1,h2,h3')
      .filter('h4')
      .each((_, el) => {
        el = $(el);
        let id = el.attr('id');
        let title = el.text();
        let contentEl = $(`
          <div id="tab-${id}">
            <div class="glue-tabpanels__panel-title">
              <h2 class="aip-tab-header">${title}</h2>
            </div>
            <div id="tab-${id}-content" class="glue-tabpanels__panel-content">
              <div></div>
            </div>
          </div>
        `);
        el.nextUntil('h1,h2,h3,h4,hr').appendTo(
          contentEl
            .children(`#tab-${id}-content`)
            .children()
            .eq(0)
        );
        tabs.push({ id, contentEl, title });
        el.remove();
      });

    // Sanity check: If there are no tabs, stop.
    if (tabs.length == 0) {
      return;
    }

    // Create the structure for the tab interface.
    let tabStruct = $(`
      <div class="glue-tabpanels" data-glue-tabpanels="${secId}">
        <ul class="glue-tabpanels__page-list">
        </ul>
        <div class="glue-tabpanels__panel-list">
        </div>
      </div>
    `);

    // Iterate over each tab and build the DOM inside the tab structure.
    for (let tab of tabs) {
      // Add the tab itself, with the title.
      $(`<li><a href="#${tab.id}">${tab.title}</a></li>`).appendTo(
        tabStruct.children('.glue-tabpanels__page-list')
      );

      // Add the tab content.
      tab.contentEl.appendTo(
        tabStruct.children('.glue-tabpanels__panel-list')
      );
    }

    // Add the tab interface in place of what was there before.
    tabStruct.insertAfter(anchor);
    anchor.remove();

    // If we needed an <hr /> to stop the final tab, expunge it.
    section
      .nextUntil('h1,h2:not(.aip-tab-header),h3,h4')
      .filter('hr')
      .remove();

    // Finally, wire up the tab interface!
    new glue.ui.tabPanels.TabPanels(tabStruct[0]);
  });
});
