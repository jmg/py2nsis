function Effect(){

	this.fade = function(css_class)
	{
		$(css_class).ready(function(){
			$(css_class).fadeIn('slow', function(){
			});
		});
	}
	
	this.slide = function(css_class, child)
	{
		$(document).ready(function(){
			$(css_class).hover(function(){
				$(this).children(child).animate({
					left: '+=20'
				}, 'fast');
			}, function(){
				$(this).children(child).animate({
					left: '-=20'
				}, 'fast');
			});
		});
	}
}