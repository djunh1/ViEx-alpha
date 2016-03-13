/**
* Post
* @namespace viex.posts.directives
*/
(function () {
  'use strict';

  angular
    .module('viex.valueFacts.directives')
    .directive('post', post);

  /**
  * @namespace Post
  */
  function post() {
    /**
    * @name directive
    * @desc The directive to be returned
    * @memberOf viex.posts.directives.Post
    */
    var directive = {
      restrict: 'E',
      scope: {
        post: '='
      },
      templateUrl: '/static/templates/valueFact/valueFact.html'
    };

    return directive;
  }
})();