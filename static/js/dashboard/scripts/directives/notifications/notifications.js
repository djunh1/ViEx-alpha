'use strict';

/**
 * @ngdoc directive
 * @name izzyposWebApp.directive:adminPosHeader
 * @description
 * # adminPosHeader
 */
angular.module('viex.theExchangeApp')
	.directive('notifications',function(){
		return {
        templateUrl:'/static/js/dashboard/scripts/directives/notifications/notifications.html',
        restrict: 'E',
        replace: true,
    	}
	});

