var btnAbrirPopup = document.getElementById('btn-sesion'),
	overlay = document.getElementById('modal_container'),
	popup = document.getElementById('popup'),
	cerrarpopup = document.getElementById('btn-cerrar');





// Initialize and add the map
function initMap() {
  // The location of Uluru
  const uluru = { lat: -25.344, lng: 131.036 };
  // The map, centered at Uluru
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 4,
    center: uluru,
  });
  // The marker, positioned at Uluru
  const marker = new google.maps.Marker({
    position: uluru,
    map: map,
  });
}






btnAbrirPopup.addEventListener('click', function(){

	modal_container.classList.add('active');	
});

cerrarpopup.addEventListener('click', function(){

	modal_container.classList.remove('active');	
});

$(function(){
	if (navigator.geolocation)
	{
		navigator.geolocation.getCurrentPosition(getCoords, getError)
	}	else{

	}

	function getCoords(position)
	{
		var lat = position.coords.latitude;
		var lng = position.coords.longitude;

		initialize(lat, lng);

	}
	
	function getError(err)
	{
		initialize(-33.5104922,-70.7520978)

	}

	function initialize(lat, lng)
	{
		var latlng = new google.maps.latlng(lat, lng);
		var mapSettings = {
			center: latlng,
			Zoom: 15,
			mapTypeId: google.maps.MapTypeId.ROADMAP
		}
		map = new google.maps.Map($('#mapa').get(0), mapSettings );
	}






});
