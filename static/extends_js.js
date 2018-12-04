function delete_thesis(url){
    var is_delete = confirm('是否删除选题！');
    if (is_delete){
        window.open(url, '_self');
    }
}


function delete_files(fileName){
    var is_delete = confirm('确定删除文件吗？');
    var url = '/delete?file=' + fileName;
    if (is_delete){
        window.open(url, '_self');
    }
}


function cancelTeacher(url, teacher_name){
    var is_concel = confirm('是否取消选择' + teacher_name + '教师，取消选择后你的论文选题将同时被取消选择');
    if (is_concel){
        window.open(url, '_self');
    }
}

function aggre_thesis(url){
    var if_aggre = confirm('确定同意该选题？')
    if (if_aggre){
        window.open(url, '_self');
    }
}


function upload_file(){
    var files = document.getElementById('uploadFile');
    var uploadFile = files.files[0];
    if (uploadFile){
        file_size = uploadFile.size; // 获取文件的大小
        if (file_size > 50*1024*1024){
            alert('上传文件不能超过50M！');
            files.outerHTML = files.outerHTML;  //清空file_input的内容
            return false;
        }else{
            var show_upload_info = document.getElementById('show-upload-info')
            var hidebg = document.getElementById('hidebg')
            hidebg.style.display = 'block';
            show_upload_info.style.display = 'block';
        }
    }else{
        alert('请添加文件！');
        return false;
    }
}


function cancel_show(){
    var show_div = document.getElementById('disggreReson');
    show_div.style.display = 'none';
}


function search_thesis(){
    var thesis_name_input = document.getElementById('thesis_name');
    var thesis_name = thesis_name_input.value.trim()
    if (thesis_name){
        window.open('?thesis_name='+thesis_name, '_self');
    }else{
        alert('不能为空');
    }
}

function search_teacher(){
    var teacher_name_input = document.getElementById('teacher_name');
    var teacher_name = teacher_name_input.value.trim();
    if (teacher_name){
        window.open('?teacher_name='+teacher_name, '_self');
    }else{
        alert('不能为空');
    }
}

function selectIndex(){
    var cookies = document.cookie;
    var select = document.getElementById('order_by_select'); 
    var cookies_array = cookies.split('; ');   //将每个cookies分隔
    for (i=0;i<cookies_array.length;i++){
        var cookie = cookies_array[i].split('=');
        if (cookie[0] == 'index'){
            select.selectedIndex = cookie[1];
            break;
        }
    }
}

function submitOrderBy(){
    var form = document.getElementById('order_by_form');
    var select = document.getElementById('order_by_select');
    var index = select.selectedIndex;
    document.cookie = 'index=' + index;   //设置cookie, key为index，值为选择的下拉框index的值
    form.submit();
}
