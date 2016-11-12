app={
	globals:{
		pageNavOriginalTop:null,
	},
	main:{
		init:function(){
			$b=$("body");
			if($b.hasClass("home"))
				app.home.init();
			if($b.hasClass("babypage")) {
				app.babypage.init();
				app.formvalidator.init();
			}
			if($b.hasClass("cadastro"))
				app.formvalidator.init();

			//smooth scroll anchor nav
			$('a[href*="#"]').on('click', function(e){
				if(window.location.pathname==this.pathname) {
					e.preventDefault();
					$('html,body').animate({scrollTop:$(this.hash).offset().top-$("nav.pagenav").height()}, 'slow', 'easeOutCubic');
				}
			});

			if($(".number-with-incbuttons").length>0)
				setupNumberWithIncButtons();

		}
	},
	home:{
		init:function(){
			$("#nav-icon3").click(function(){
				$t=$(this);
				$t.toggleClass("open");
				$("header.main nav").slideToggle();
			});
		}
	},
	babypage:{
		init:function(){
			//sticky nav
			app.globals.pageNavOriginalTop = app.globals.pageNavOriginalTop==null ? $("nav.pagenav").offset().top : app.globals.pageNavOriginalTop; //runonce
			updateStickyNav();

			//notification bubble
			$(".notifications .balloon").unbind().click(function(e){
				e.preventDefault();
				$(".notifications-popup").toggleClass("opened").slideToggle('fast');
			})
			$(".mCustomScrollbar").mCustomScrollbar({'theme':'minimal-dark'});

			//family carousel
			$(".familiaslideshow ul").owlCarousel({
				navigation:true,
				navigationText:['<i class="icon-angle-left"></i>','<i class="icon-angle-right"></i>'],
				rewindNav:false,
				scrollPerPage:true,
				slideSpeed:1000,
				afterInit:function(){$(this.$elem[0]).css('visibility','visible')}
			});

			$(".eventos-slider ul").owlCarousel({
				navigation:true,
				navigationText:['<i class="icon-angle-left"></i>','<i class="icon-angle-right"></i>'],
				rewindNav:false,
				scrollPerPage:true,
				slideSpeed:1000,
				items:1,
				// loop:false,
				// afterInit:function(){$(this.$elem[0]).css('visibility','visible')}
			});

			// TROCA PAINEL DE VIEW PRA EDIT
			$(".editpanelink,.meuseventos .button.add").unbind().click(function(e){
				e.preventDefault();
				$s=$(this).closest("section");
				$s.fadeOut('slow',function(){
					$s.load("parts/"+$s.data("form"),function() {
						$(this).children(':first').unwrap().hide().fadeIn('slow');
						app.main.init()
					})
				})
			})

			//TROCA PAINEL DE EDIT PRA VIEW
			$(".cancelpanellink,button.cancel").unbind().click(function(e){
				e.preventDefault();
				$s=$(this).closest("section");
				$s.fadeOut('slow',function(){
					$s.load("parts/"+$s.data("view"),function() {
						$(this).children(':first').unwrap().hide().fadeIn('slow');
						app.main.init()
					})
				})
			})

			app.formfamilia.init();

			$(".user .avatar").unbind().click(function(){
				$(this).closest(".user").toggleClass("opened").find(".userdropdown").slideToggle('fast');
			})
		}
	},
	formfamilia:{
		init:function(){
			$formfamilia = $("section.form.minhafamilia");
			$formfamilia.find(".button.add").unbind().click(function(){
				$row = $($formfamilia.find("form .rowwrapper>*:first-child").get(0));
				$row.clone().insertAfter( $formfamilia.find("form .rowwrapper>*:last-child") );
				app.formfamilia.init($formfamilia);
			})
			$formfamilia.find(".remove").click(function(){
				$(this).closest(".row").remove();
			})
		}
	},
	formvalidator:{
		init:function(){
			$("form").validator({
				focus:false,
				feedback: {
					success: 'icon-plus',
					error: 'icon-plus'
				}
			});
			$('form').validator().on('submit', function (e) {
				if (e.isDefaultPrevented()) {
				// handle the invalid form...
				} else {
				// everything looks good!
				}
			})
		}
	}
};

$(app.main.init);

$(window).scroll(updateStickyNav);

function updateStickyNav(){
	if($(window).scrollTop()>=app.globals.pageNavOriginalTop)
		$("nav.pagenav").addClass("sticky");
	else
		$("nav.pagenav").removeClass("sticky");
}

function setupNumberWithIncButtons(){
	$o=$(".number-with-incbuttons");
	$i=$o.find("input");
	$o.find(".dec").click(function(){
		$i.val(Math.max(1,Number($i.val())-1));
	});
	$o.find(".inc").click(function(){
		$i.val(Number($i.val())+1);
	});
}