(function () {
  'use strict';

  angular.module('viex.layout.controllers', [])
    .controller('TabsCtrl', ['$scope', function ($scope) {
        $scope.tabs = [{
                number:'1',
                title: 'Overview',
                url: 'one.tpl.html'
            }, {
                number:'2',
                title: 'Management',
                url: 'two.tpl.html'
            }, {
                number:'3',
                title: 'Financials',
                url: 'three.tpl.html'
            },
            {
                number:'4',
                title: 'Customers',
                url: 'four.tpl.html'
            },
            {
                number:'5',
                title: 'Products',
                url: 'five.tpl.html'
            },
            {
                number:'6',
                title: 'Industry',
                url: 'six.tpl.html'
            },
            {
                number:'7',
                title: 'Growth',
                url: 'seven.tpl.html'
            },


        ];

        $scope.currentTab = 'one.tpl.html';

        $scope.onClickTab = function (tab) {
            $scope.currentTab = tab.url;
        }

        $scope.isActiveTab = function(tabUrl) {
            return tabUrl == $scope.currentTab;
        }
        }]);


})();