(function () {
  'use strict';

  angular
    .module('viex.authentication.services')
    .factory('Authentication', Authentication);

  Authentication.$inject = ['$cookies', '$http'];

  /**
  * @namespace Authentication
  * @returns {Factory}
  */
  function Authentication($cookies, $http) {
    /**
    * @name Authentication
    * @desc The Factory to be returned
    */
    var Authentication = {
        getAuthenticatedAccount: getAuthenticatedAccount,
        isAuthenticated: isAuthenticated,
        login: login,
        logout:logout,
        register: register,
        setAuthenticatedAccount: setAuthenticatedAccount,
        unauthenticate: unauthenticate
    };

    return Authentication;

    ////////////////////

    function register(email, password, username) {
      return $http.post('/api/v1/accounts/', {
        username: username,
        password: password,
        email: email
      }).then(registerSuccessFn, registerErrorFn);

          function registerSuccessFn(data, status, headers, config) {
            Authentication.login(email, password);
          }

          function registerErrorFn(data, status, headers, config) {
            console.error('Cant do that');
          }
    }


    function login(email, password) {
        return $http.post('/api/v1/auth/login/',{
            email:email, password:password
         }).then(loginSuccessFn, loginErrorFn);

        function loginSuccessFn(data, status, headers, config) {
             Authentication.setAuthenticatedAccount(data.data);

             window.location = '/';
         }

        function loginErrorFn(data, status, headers, config) {
           console.error(data)
           console.error(status)
           console.error(headers)
           console.error(config)
           console.error('All board the fail boat.');
         }
     }


     function logout() {
          return $http.post('/api/v1/auth/logout/')
            .then(logoutSuccessFn, logoutErrorFn);

          /**
           * @name logoutSuccessFn
           * @desc Unauthenticate and redirect to index with page reload
           */
          function logoutSuccessFn(data, status, headers, config) {
            Authentication.unauthenticate();

            window.location = '/';
          }

          function logoutErrorFn(data, status, headers, config) {
            console.error('Error while logging out');
          }
        }

    function getAuthenticatedAccount() {
       if (!$cookies.authenticatedAccount) {
         return;
       }

       return JSON.parse($cookies.authenticatedAccount);
     }

    function isAuthenticated() {
       return !!$cookies.authenticatedAccount;
    }

    function setAuthenticatedAccount(account) {
       $cookies.authenticatedAccount = JSON.stringify(account);
    }

    function unauthenticate() {
      delete $cookies.authenticatedAccount;
    }

  }
})();
