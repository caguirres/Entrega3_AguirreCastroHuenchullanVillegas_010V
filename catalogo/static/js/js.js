var btnAbrirPopup = document.getElementById('btn-sesion'),
	overlay = document.getElementById('modal_container'),
	popup = document.getElementById('popup'),
	cerrarpopup = document.getElementById('btn-cerrar');


btnAbrirPopup.addEventListener('click', function(){

	modal_container.classList.add('active');	
});

cerrarpopup.addEventListener('click', function(){

	modal_container.classList.remove('active');	
});


