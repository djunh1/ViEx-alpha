(function () {
  'use strict';

  angular
    .module('viex.valueFacts', [
      'viex.valueFacts.controllers',
      'viex.valueFacts.directives',
      'viex.valueFacts.services'
    ]);

  angular
    .module('viex.valueFacts.controllers', []);

  angular
    .module('viex.valueFacts.directives', ['ngDialog']);

  angular
    .module('viex.valueFacts.services', []);
})();