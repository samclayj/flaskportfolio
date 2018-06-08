const ScrollIn = (function() {

    let scrollInBehavior = function(pageTop, pageBottom) {
        const tags = $(".scroll-in");

        for (const tag of tags) {
            if ($(tag).position().top < pageBottom) {
                $(tag).addClass("visible");
            } else {
                $(tag).removeClass("visible");
            }
        }
    }

    return {
        scrollInBehavior: scrollInBehavior,
    }
})();
