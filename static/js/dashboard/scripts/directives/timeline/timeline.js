'use strict';

/**
 * @ngdoc directive
 * @name izzyposWebApp.directive:adminPosHeader
 * @description
 * # adminPosHeader
 */
angular.module('viex.theExchangeApp')
	.directive('timeline',function() {
    return {
        templateUrl:'/static/js/dashboard/scripts/directives/timeline/timeline.html',
        restrict: 'E',
        replace: true,
    }
  });