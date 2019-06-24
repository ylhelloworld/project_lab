var gulp = require('gulp');
var concat = require('gulp-concat');


gulp.task('concat', function() {  
    // 你的默认的任务代码放在这  
    gulp.src('src/*.js')   
        .pipe(concat('bundle.js'))  
        .pipe(gulp.dest('dest'));  
});  
  
gulp.task('default', ['concat']);  