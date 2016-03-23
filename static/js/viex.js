
(function () {
  'use strict';


  angular
    .module('viex', [
      'viex.config',
      'viex.routes',
      'viex.authentication',
      'viex.layout',
      'viex.utils',
      'viex.valueFacts',
      'viex.profiles',
      'viex.aboutfaq'



    ]);

  angular
    .module('viex.config', []);

  angular
    .module('viex.routes', ['ngRoute']);


  angular
  .module('viex')
  .run(run);

run.$inject = ['$http'];

function run($http) {
  $http.defaults.xsrfHeaderName = 'X-CSRFToken';
  $http.defaults.xsrfCookieName = 'csrftoken';
}
})();