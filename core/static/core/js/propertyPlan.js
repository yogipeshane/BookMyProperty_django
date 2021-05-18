console.log(" In property Plan.............................")




///*$.ajax({
//  url: "http://127.0.0.1:5555/property/plan/",
//  headers: {"Access-Control-Allow-Origin": "**/*//*"},
//  contentType: "application/json",
//  success: function(data){
//        console.log(data)
//    }

//  })*/


jQuery.support.cors = true;
$.ajax({
url: "http://127.0.0.1:5555/property/plan/",
type: "GET",
dataType: "json",
contentType: "application/json",

// data: { order: orderData },
success: function (response) {
alert(response.OrderPlacementResult);
// orderId = data;
if (data != null) {
orderStatus = "Order has been placed successfully.";
}
}

});