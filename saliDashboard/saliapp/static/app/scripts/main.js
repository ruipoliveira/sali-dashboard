/**
 * Created by roliveira on 2/16/17.
 */

var js_list = {{django_list}};


function myMap() {
    var mapProp= {
        center:new google.maps.LatLng(40.64258200399365,-8.656024932861328),
        zoom:10,
    };
    var map=new google.maps.Map(document.getElementById("googleMap"),mapProp);
}

function PopUp(){
    document.getElementByID("addForm").showModal();
}