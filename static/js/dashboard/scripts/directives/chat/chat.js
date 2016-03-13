'use strict';

/**
 * @ngdoc directive
 * @name izzyposWebApp.directive:adminPosHeader
 * @description
 * # adminPosHeader
 */
angular.module('viex.theExchangeApp')
	.directive('chat',function(){
		return {
        templateUrl:'/static/js/dashboard/scripts/directives/chat/chat.html',
        restrict: 'E',
        replace: true,
    	}
	});