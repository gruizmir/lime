$(document).ready(function() {
	
	$('a[rel*=external]').click( function() {
        window.open(this.href);
        return false;
    });
    
	var example = $('#areas'), defaults = {
		buildComplete: function () {
			example.css('visibility', 'visible');
		},
		timeout: 5500
	};
	function build(x) {
		var opts, current;
		if (!$.isEmptyObject(example.data())) { /* If an zAccordion is found, rebuild it with new settings. */
			example.css('visibility', 'hidden');
			current = example.data('current');
			opts = $.extend({
				startingSlide: current
			}, defaults, x);
			example.zAccordion('destroy', {
				removeStyleAttr: true,
				removeClasses: true,
				destroyComplete: {
					afterDestroy: function() {
						try {
							console.log('zAccordion destroyed! Attempting to rebuild...');
						} catch (e) {}
					},
					rebuild: opts
				}
			});
		} else { /* If no zAccordion is found, build one from scratch. */
			example.css('visibility', 'hidden');
			opts = $.extend(defaults, x);
			example.zAccordion(opts);
		}
	}
	/* A unique Media Query is registered for each screen size. */
	enquire.register('screen and (min-width: 960px)', { /* Standard screen sizes and a default build for browsers that are unsupported. */
		match : function () {
			build({
				slideWidth: 540,
				width: 1180,
				height: 350
			});
		} /* The *true* value below means this media query will fire by default. */
	}, true).register('screen and (min-width: 768px) and (max-width: 959px)', {
		match : function () {
			build({
				slideWidth: 420,
				width: 680,
				height: 200
			});
		}
	}).register('screen and (min-width: 480px) and (max-width: 767px)', {
		match : function () {
			build({
				slideWidth: 220,
				width: 380,
				height: 200
			});
		}
	}).register('screen and (max-width: 479px)', {
		match : function () {
			if (!$.isEmptyObject(example.data())) {
				example.zAccordion('destroy', {
					removeStyleAttr: true,
					removeClasses: true,
					destroyComplete: {
						afterDestroy: function() {
							try {
								console.log('zAccordion destroyed!');
							} catch (e) {}
						}
					}
				});
			}
		}
	}).listen(5);
	// Skrollr
	var s = skrollr.init({
		edgeStrategy: 'set',
		easing: {
			WTF: Math.random,
			inverted: function(p) {
				return 1-p;
			}
		}
	});
});
