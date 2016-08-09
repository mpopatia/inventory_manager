/**
 * Created by musab on 09/08/16.
 */

var app = angular.module('manager', []);

app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
  });


app.controller('ItemController', [ '$http', function($http){
    var item_controller = this
    item_controller.items_array = [];

    $http.get('/manager/get_items').success(function(data){
        console.log(data);
        item_controller.items_array = data;
    });
}]);