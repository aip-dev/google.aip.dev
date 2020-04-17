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
  for (let callout of ['Important', 'Note', 'TL;DR', 'Warning', 'Summary']) {
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
});
