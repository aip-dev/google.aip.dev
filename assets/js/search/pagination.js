// Copyright 2020 Google LLC
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

// This file contains JavaScript that makes the search boxes work better.
// It causes the entire <li /> to be clickable instead of just the link.
// (We do not control the HTML so this is the best option.)
$.when($.ready).then(() => {
  $(document).on(
    'click',
    '#tipue_search_foot_boxes li:not(.current)',
    function () {
      $(this).children('a').eq(0).click();
    }
  );
});
