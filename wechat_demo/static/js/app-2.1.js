function timeStamp2String(time){  
    var datetime = new Date();  
    datetime.setTime(time);  
    var year = datetime.getFullYear();  
    var month = datetime.getMonth() + 1 < 10 ? "0" + (datetime.getMonth() + 1) : datetime.getMonth() + 1;  
    var date = datetime.getDate() < 10 ? "0" + datetime.getDate() : datetime.getDate();  
    var hour = datetime.getHours()< 10 ? "0" + datetime.getHours() : datetime.getHours();  
    var minute = datetime.getMinutes()< 10 ? "0" + datetime.getMinutes() : datetime.getMinutes();  
    var second = datetime.getSeconds()< 10 ? "0" + datetime.getSeconds() : datetime.getSeconds();  
    return year + "-" + month + "-" + date+" "+hour+":"+minute+":"+second;  
}

function ServerTimeSync() {
    ServerTimeLimit = ServerTimeLimit + 1000;
    if ($('.server-time').is(':visible')) {
        $('.server-time').html(timeStamp2String(ServerTimeLimit));
        setTimeout('ServerTimeSync();', 1000);
    }
}
/* ======================================================= */
var App = function() {
    var e, a, i, s, t, l, o, r, n, d = function() {
        e = $("#page-container"), i = $("header"), a = $("#page-content"), s = $("#sidebar"), t = $("#sidebar-brand"), l = $("#sidebar-extra-info"), r = $("#sidebar-scroll"), o = $("#sidebar-alt"), n = $("#sidebar-scroll-alt"), m(), p("init"), c(),
        (i.hasClass("navbar-fixed-top") || i.hasClass("navbar-fixed-bottom")) && $(window).on("scroll",
        function() {
            $(this).scrollTop() > 50 ? i.addClass("navbar-glass") : i.removeClass("navbar-glass")
        }),
        $(window).on("resize orientationchange",
        function() {
            g()
        }).resize();
        var d = $("#year-copy"),
        h = new Date;
        d.html("2009-" + h.getFullYear().toString()),
        b($(".btn-effect-ripple"), "btn-ripple"),
        $('[data-toggle="tabs"] a, .enable-tabs a').click(function(e) {
            e.preventDefault(),
            $(this).tab("show")
        }),
        $('[data-toggle="tooltip"], .enable-tooltip').tooltip({
            container: "body",
            animation: !1
        }),
        $('[data-toggle="popover"], .enable-popover').popover({
            container: "body",
            animation: !0
        }),
        true
    },
    h = function() {
        var a = $("#page-wrapper");
        a.hasClass("page-loading") && (e.hasClass("enable-cookies") ? setTimeout(function() {
            a.removeClass("page-loading")
        },
        100) : a.removeClass("page-loading"))
    },
    c = function() {
        var a = $(".sidebar-nav a", s),
        i = $(".sidebar-nav-menu", s),
        t = $(".sidebar-nav-submenu", s);
        i.on("click",
        function() {
            var a = $(this),
            i = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
            return e.hasClass("sidebar-visible-lg-mini") && i > 991 ? a.hasClass("open") ? a.removeClass("open") : ($("#sidebar .sidebar-nav-menu.open").removeClass("open"), a.addClass("open")) : a.parent().hasClass("active") || (a.hasClass("open") ? a.removeClass("open") : ($("#sidebar .sidebar-nav-menu.open").removeClass("open"), a.addClass("open")), setTimeout(g, 50)),
            !1
        }),
        t.on("click",
        function() {
            var e = $(this);
            return e.parent().hasClass("active") !== !0 && (e.hasClass("open") ? e.removeClass("open") : (e.closest("ul").find(".sidebar-nav-submenu.open").removeClass("open"), e.addClass("open")), setTimeout(g, 50)),
            !1
        })
    },
    b = function(e, a) {
        e.css({
            overflow: "hidden",
            position: "relative"
        }),
        e.on("click",
        function(e) {
            var i, s, t, l, o = $(this);
            0 == o.children("." + a).length ? o.prepend('<span class="' + a + '"></span>') : o.children("." + a).removeClass("animate");
            var i = o.children("." + a);
            i.height() || i.width() || (s = Math.max(o.outerWidth(), o.outerHeight()), i.css({
                height: s,
                width: s
            })),
            t = e.pageX - o.offset().left - i.width() / 2,
            l = e.pageY - o.offset().top - i.height() / 2,
            i.css({
                top: l + "px",
                left: t + "px"
            }).addClass("animate")
        })
    },
    p = function(a) {
        if ("init" === a) {
            p("sidebar-scroll"),
            p("sidebar-alt-scroll");
            var s;
            $(window).on("resize orientationchange",
            function() {
                clearTimeout(s),
                s = setTimeout(function() {
                    p("sidebar-scroll")
                },
                150)
            })
        } else {
            var d = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
            if ("toggle-sidebar" === a) d > 991 ? (e.hasClass("sidebar-visible-lg-full") ? e.removeClass("sidebar-visible-lg-full").addClass("sidebar-visible-lg-mini") : e.hasClass("sidebar-visible-lg-mini") ? e.removeClass("sidebar-visible-lg-mini").addClass("sidebar-visible-lg-full") : e.addClass("sidebar-visible-lg-mini"), setTimeout(g, 50)) : (e.toggleClass("sidebar-visible-xs"), e.hasClass("sidebar-visible-xs") && p("close-sidebar-alt")),
            p("sidebar-scroll");
            else if ("open-sidebar" === a) d > 991 ? e.removeClass("sidebar-visible-lg-mini").addClass("sidebar-visible-lg-full") : (e.addClass("sidebar-visible-xs"), p("close-sidebar-alt")),
            p("sidebar-scroll"),
            setTimeout(g, 50);
            else if ("close-sidebar" === a) d > 991 ? e.removeClass("sidebar-visible-lg-full").addClass("sidebar-visible-lg-mini") : e.removeClass("sidebar-visible-xs"),
            p("sidebar-scroll");
            else if ("toggle-sidebar-alt" === a) d > 991 ? e.toggleClass("sidebar-alt-visible-lg") : (e.toggleClass("sidebar-alt-visible-xs"), e.hasClass("sidebar-alt-visible-xs") && p("close-sidebar"));
            else if ("open-sidebar-alt" === a) d > 991 ? e.addClass("sidebar-alt-visible-lg") : (e.addClass("sidebar-alt-visible-xs"), p("close-sidebar"));
            else if ("close-sidebar-alt" === a) e.removeClass(d > 991 ? "sidebar-alt-visible-lg" : "sidebar-alt-visible-xs");
            else if ("sidebar-scroll" == a) {
                if (e.hasClass("sidebar-visible-lg-mini") && d > 991) r.length && r.parent(".slimScrollDiv").length && (r.slimScroll({
                    destroy: !0
                }), r.attr("style", ""));
                else if (i.hasClass("navbar-fixed-top") || i.hasClass("navbar-fixed-bottom")) {
                    var h = $(window).height() - (("none" === t.css("display") ? 0 : t.outerHeight()) + ("none" === l.css("display") ? 0 : l.outerHeight()));
                    992 > d && (h -= 50),
                    r.length && !r.parent(".slimScrollDiv").length ? r.slimScroll({
                        height: h,
                        color: "#bbbbbb",
                        size: "3px",
                        touchScrollStep: 100,
                        railVisible: !1,
                        railOpacity: 1
                    }) : r.add(r.parent()).css("height", h)
                }
            } else if ("sidebar-alt-scroll" == a) if (n.length && !n.parent(".slimScrollDiv").length) {
                n.slimScroll({
                    height: o.outerHeight(),
                    color: "#bbbbbb",
                    size: "3px",
                    touchScrollStep: 100,
                    railVisible: !1,
                    railOpacity: 1
                });
                var c;
                $(window).on("resize orientationchange",
                function() {
                    clearTimeout(c),
                    c = setTimeout(function() {
                        p("sidebar-alt-scroll")
                    },
                    150)
                })
            } else n.add(n.parent()).css("height", o.outerHeight())
        }
    },
    g = function() {
        var e = $(window).height(),
        t = i.outerHeight(),
        l = s.outerHeight();
        i.hasClass("navbar-fixed-top") || i.hasClass("navbar-fixed-bottom") ? a.css("min-height", e) : l > e ? a.css("min-height", l - t) : a.css("min-height", e - t)
    },
    m = function() {},
    v = function() {};
    return {
        init: function() {
            d(), h()
        },
        sidebar: function(e, a) {
            p(e, a)
        }
    }
} ();
$(function() {
    App.init();
    // WXAD
    $("#jswx_container").remove();
    $("#icr_r_div").remove();
});