/**
 * Created by kimxu on 2016/11/18.
 */



// $("#navbar").find("li:first").addClass("active");
// $("#navbar").find('li').click(function () {
//     $("#navbar").find("li").removeClass("active");
//     $(this).addClass('active');
// });

var value = $("#formServerCategory").text();
$("#navbar").find("li").removeClass("active");
if (value == "技术") {
    $("#navbar").find("li:first").addClass("active");
} else if (value == "生活") {
    $("#navbar").find("li:eq(1)").addClass("active");
} else if (value == "杂谈") {
    $("#navbar").find("li:eq(2)").addClass("active");
}else if (value == "标签云") {
    $("#navbar").find("li:eq(3)").addClass("active");
}else if (value == "关于") {
    $("#navbar").find("li:eq(4)").addClass("active");
}
