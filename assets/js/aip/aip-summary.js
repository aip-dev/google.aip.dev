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

// This file contains JavaScript-applied rules that apply to the AIP site
// specifically.
$.when($.ready).then(() => {
  // Each AIP has an "AIP Summary".
  // Apply a class to it for styling.
  $("table th:first-child:contains(AIP Summary)")
    .parents("table")
    .attr("id", "aip-summary")
    .addClass("no-h")
    .insertBefore("#aip-toc");
  // .insertAfter("#aip-main h1:eq(0)");

  // Cause the AIP summary header to span all columns.
  // (This is trivial in HTML but impossible in Markdown.)
  $("#aip-summary th").each(function() {
    $(this)
      .attr("colspan", ($(this).siblings().length + 1).toString())
      .nextAll()
      .detach();
    return false;
  });
});
