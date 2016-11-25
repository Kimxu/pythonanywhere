/**
 * Created by kimxu on 2016/11/15.
 */

angular.module('App', [])
    .controller('PostController', function ($scope, $http, $sce) {
        var datas = $("#tags").text().split('?');
        var data = datas[0];
        $scope.getDatas = function (pager) {
            //判断是否还有上一页
            if (pager == 0)
                $scope.noPre = true;
            else
                $scope.noPre = false;
            $http.get('/posts/tag/' + data + "?pager=" + pager).success(function (data) {
                if (data.nextPagerDatas) {
                    alert("下一页没数据了");
                    $scope.pager = $scope.pager - 1;
                    $scope.hasPager = true;
                } else {
                    if (data.noDatas) {
                        $scope.articles = $sce.trustAsHtml(NO_DATAS_ITEM_TEMPLATE);
                    } else {
                        var datas = renderArticleItem(data['articles']);
                        $scope.articles = $sce.trustAsHtml((datas[0]));
                        $scope.counts = datas[1];
                        $scope.hasPager = !$scope.noPre || data.hasPager;
                    }
                }
            }).error(function (err) {
                $scope.error = 'Could not load notes';
            });
        };

        if (datas.size > 1) {
            $scope.pager = datas[1];
            $scope.getDatas($scope.pager);
        } else {
            $scope.pager = 0;
            $scope.getDatas($scope.pager);
        }


        var ARTICLE_ITEM_TEMPLATE =
            "<div class='card' style='background-color: #ffffff;margin: 15px;border-radius: 5px'>" +
            "<div class='card-header' style='background-color: #f0f0f0;padding: 5px'>" +
            "<span><a class='h2 ls-article-title' href='/posts/{articleId}/'>{title}</a></span>" +
            "</div>" +
            "<div class='article-property'  style='padding: 5px;'><p style='font-size: 16px;color: #2b2b2b'>{summary}</p></div></br>" +
            "<div class='card-block' style='padding: 10px'>" +
            "<span class='article-property' title='作者' style='color: #2a2a2a'><i class='fa fa-user'></i> {author} </span>" +
            "<span class='article-property' title='标签' style='color: #2b2b2b'><i class='fa fa-tags'></i> {tags} </span>" +
            "<div class='card-block text-right' style='float: right'>" +
            "<p style='color: #2b2b2b'>{modify_time}</p>" +
            "</div>" +
            "</div>" +
            "</div>" +
            "</div>";

        var NO_DATAS_ITEM_TEMPLATE =
            "<div class='card' style='background-color: #ffffff;margin: 15px;border-radius: 5px'>" +
            "<div class='card-header' style='background-color: #f0f0f0;padding: 5px'>" +
            "<span>该栏目目前没有文章~</span>" +
            "</div>" +
            "</div>";
        var TAG_TEMPLATE = "<a href='/tags/{tag}/' class='tag-index'>{tag}&nbsp</a>";
        var AUTHOR_TEMPLATE = "<a href='/about/user' class='author-index'>{author}</a>";

        function renderTags(tags) {
            var tagHtml = "";
            for (var i = 0; i < tags.length; i++) {
                tagHtml += TAG_TEMPLATE.replace(/\{tag}/g, tags[i]);
            }
            return tagHtml;
        }

        function renderAuthors(authors) {
            var authorHtml = "";
            for (var i = 0; i < authors.length; i++) {
                authorHtml += AUTHOR_TEMPLATE.replace(/\{author}/g, authors[i]);
            }
            return authorHtml;
        }


        function sort(data) {
            var separator = "{#}";
            var ls = [];
            for (var k in data) {
                ls.push(data[k]["publish_date"] + separator + k);
            }
            ls.sort();

            var sortedData = [];
            for (var i = ls.length - 1; i >= 0; i--) {
                var key = ls[i].split(separator)[1];
                sortedData.push(data[key]);
            }
            return sortedData;

        }

        function renderArticleItem(data) {
            var data = sort(data);
            var articleHtml = "";
            var count = 0;
            for (var key in data) {

                if (data[key]["title"].length > 0) {

                    articleHtml += ARTICLE_ITEM_TEMPLATE.replace(/\{articleId}/g, key)
                        .replace(/\{title}/g, data[key]["title"])
                        .replace(/\{modify_time}/g, data[key]["publish_date"])
                        .replace(/\{author}/g, renderAuthors(data[key]["authors"]))
                        .replace(/\{summary}/g, data[key]["summary"])
                        .replace(/\{tags}/g, renderTags(data[key]["tags"]));
                    count++;
                }
            }
            return [articleHtml, count];
        }


        $scope.nextPager = function () {
            $scope.pager = $scope.pager + 1;
            $scope.getDatas($scope.pager);
        };

        $scope.previousPager = function () {
            $scope.pager = $scope.pager - 1;
            $scope.getDatas($scope.pager);
        };
    });

