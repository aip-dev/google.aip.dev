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

// This file contains JavaScript-applied rules that apply to the AIP index
// specifically.
$.when($.ready).then(() => {
  // The base README page should have tables that span the full width
  // and look consistent with one another.
  for (let topLeftCell of ['Number', 'Block']) {
    $(`table th:first-child:contains(${topLeftCell})`)
      .parents('table')
      .addClass('aip-listing');
  }
});
