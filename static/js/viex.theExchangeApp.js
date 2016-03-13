'use strict';
/**
 * @ngdoc overview
 * @name viex.theExchangeApp
 * @description
 * # viex.theExchangeApp
 *
 * Main module of the application.
 */
angular
    .module('viex.theExchangeApp', [
    'oc.lazyLoad',
    'ui.router',
    'ui.bootstrap',
    'angular-loading-bar',
  ])
  .config(['$stateProvider','$urlRouterProvider','$ocLazyLoadProvider',function ($stateProvider,$urlRouterProvider,$ocLazyLoadProvider) {

    $ocLazyLoadProvider.config({
      debug:false,
      events:true,
    });

    $urlRouterProvider.otherwise('/dashboard/home');

    $stateProvider
      .state('dashboard', {
        url:'/dashboard',
        templateUrl: '/static/js/dashboard/views/dashboard/main.html',
        resolve: {
            loadMyDirectives:function($ocLazyLoad){
                return $ocLazyLoad.load(
                {
                    name:'viex.theExchangeApp',
                    files:[
                    '/static/js/dashboard/scripts/directives/sidebar/sidebar.js',
                    '/static/js/dashboard/scripts/directives/sidebar/sidebar-search/sidebar-search.js'
                    ]
                }),
                $ocLazyLoad.load(
                {
                   name:'toggle-switch',
                   files:["/static/bower_components/angular-toggle-switch/angular-toggle-switch.min.js",
                          "/static/bower_components/angular-toggle-switch/angular-toggle-switch.css"
                      ]
                }),
                $ocLazyLoad.load(
                {
                  name:'ngAnimate',
                  files:['/static/bower_components/angular-animate/angular-animate.js']
                })
                $ocLazyLoad.load(
                {
                  name:'ngCookies',
                  files:['/static/bower_components/angular-cookies/angular-cookies.js']
                })
                $ocLazyLoad.load(
                {
                  name:'ngResource',
                  files:['/static/bower_components/angular-resource/angular-resource.js']
                })
                $ocLazyLoad.load(
                {
                  name:'ngSanitize',
                  files:['/static/bower_components/angular-sanitize/angular-sanitize.js']
                })
                $ocLazyLoad.load(
                {
                  name:'ngTouch',
                  files:['/static/bower_components/angular-touch/angular-touch.js']
                })
            }
        }
    })
      .state('dashboard.home',{
        url:'/home',
        controller: 'MainCtrl',
        templateUrl:'/static/js/dashboard/views/dashboard/home.html',
        resolve: {
          loadMyFiles:function($ocLazyLoad) {
            return $ocLazyLoad.load({
              name:'viex.theExchangeApp',
              files:[
              '/static/js/dashboard/scripts/controllers/main.js',
              '/static/js/dashboard/scripts/directives/timeline/timeline.js',
              '/static/js/dashboard/scripts/directives/notifications/notifications.js',
              '/static/js/dashboard/scripts/directives/chat/chat.js',
              '/static/js/dashboard/scripts/directives/dashboard/stats/stats.js'
              ]
            })
          }
        }
      })
      .state('dashboard.form',{
        templateUrl:'/static/js/dashboard/views/form.html',
        url:'/form'
    })
      .state('dashboard.blank',{
        templateUrl:'/static/js/dashboard/views/pages/blank.html',
        url:'/blank'
    })
      .state('dashboard.chart',{
        templateUrl:'/static/js/dashboard/views/chart.html',
        url:'/chart',
        controller:'ChartCtrl',
        resolve: {
          loadMyFile:function($ocLazyLoad) {
            return $ocLazyLoad.load({
              name:'chart.js',
              files:[
                '/static/bower_components/angular-chart.js/dist/angular-chart.min.js',
                '/static/bower_components/angular-chart.js/dist/angular-chart.css'
              ]
            }),
            $ocLazyLoad.load({
                name:'viex.theExchangeApp',
                files:['/static/js/dashboard/scripts/controllers/chartContoller.js']
            })
          }
        }
    })
      .state('dashboard.table',{
        templateUrl:'/static/js/dashboard/views/table.html',
        url:'/table'
    })
      .state('dashboard.panels-wells',{
          templateUrl:'/static/js/dashboard/views/ui-elements/panels-wells.html',
          url:'/panels-wells'
      })
      .state('dashboard.buttons',{
        templateUrl:'/static/js/dashboard/views/ui-elements/buttons.html',
        url:'/buttons'
    })
      .state('dashboard.notifications',{
        templateUrl:'/static/js/dashboard/views/ui-elements/notifications.html',
        url:'/notifications'
    })
      .state('dashboard.typography',{
       templateUrl:'/static/js/dashboard/views/ui-elements/typography.html',
       url:'/typography'
   })
      .state('dashboard.icons',{
       templateUrl:'/static/js/dashboard/views/ui-elements/icons.html',
       url:'/icons'
   })
      .state('dashboard.grid',{
       templateUrl:'/static/js/dashboard/views/ui-elements/grid.html',
       url:'/grid'
   })
  }]);