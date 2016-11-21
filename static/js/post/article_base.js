/**
 * Created by kimxu on 2016/11/16.
 */

$(".toc ul").addClass("nav");
$(".toc ul:first").addClass("bs-docs-sidenav");
$("table").addClass("table table-striped table-bordered table-hover");

//
$('#directory').affix({
    offset: {
        top: $('#directory').offset().top,
        bottom: $('.navbar').outerHeight(true) + 40
    }
});