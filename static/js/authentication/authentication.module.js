(function () {
  'use strict';

  angular
    .module('viex.authentication', [
      'viex.authentication.controllers',
      'viex.authentication.services'
    ]);

  angular
    .module('viex.authentication.controllers', []);

  angular
    .module('viex.authentication.services', ['ngCookies']);
})();