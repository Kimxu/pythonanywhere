title: 日常问题解决
summary: 介绍本博客的基本功能
authors: Kimxu
publish_date: 2016-01-05
categories: 技术
tags: Android


`前言：开发中遇见的一些问题，都会集中在这个帖子中。`

#1. 设置Dialog的位置
     
``` JAVA
  YYHLoginDialog mLoginDialog = new YYHLoginDialog(mActivity);
  Window dialogWindow = mLoginDialog.getWindow();
  WindowManager.LayoutParams lp = dialogWindow.getAttributes();
  //背景无遮罩
  dialogWindow.clearFlags(WindowManager.LayoutParams.FLAG_DIM_BEHIND);
  dialogWindow.setGravity(Gravity.CENTER_HORIZONTAL | Gravity.TOP);
  lp.y = GlobalUtils.convertDipOrPx(mActivity, 80);
  dialogWindow.setAttributes(lp);
```
  
  这么设置的没有问题，如果把：
     
``` JAVA
  WindowManager.LayoutParams lp = dialogWindow.getAttributes();
```
     
  替换成：
     
``` JAVA
  WindowManager.LayoutParams lp = new WindowManager.LayoutParams();
```
     
  就会出现背景是黑色的问题。
   
#2. startActivityForResult() 后直接调用 onActivityResult()
   
   这个问题是在开发中偶然遇见的问题。调用startActivityForResult()方法后，直接就调用了onActivityResult()。后来找到了原因，是因为启动的目标Activity设置了加载模式（launchMode）。启动的Activity*只能使用标准模式*。
   
#3. 获得状态栏高度
     
``` JAVA
  public static int getStatusBar(Context context) {
          Class<?> c = null;
          Object obj = null;
          Field field = null;
          int x = 0, sbar = 0;
          try {
              c = Class.forName("com.android.internal.R$dimen");
              obj = c.newInstance();
              field = c.getField("status_bar_height");
              x = Integer.parseInt(field.get(obj).toString());
              sbar = context.getResources().getDimensionPixelSize(x);
              return sbar;
          } catch (Exception e1) {
              Log.e("Tag", "get status bar height fail");
              e1.printStackTrace();
              return 0;
          }
      }
```

   
   ​
