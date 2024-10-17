document.getElementById('accessibleBtn').addEventListener('click', () => {
    fetch('http://localhost:9991/ok')
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerText = data.message;
        })
        .catch(error => {
            document.getElementById('result').innerText = '错误: ' + error;
        });
});

document.getElementById('notAccessibleBtn').addEventListener('click', () => {
    fetch('http://localhost:9991/o')
        .then(response => {
            if (!response.ok) {
                throw new Error('接口不可访问');
            }
            return response.json();
        })
        .then(data => {
            document.getElementById('result').innerText = data.message;
        })
        .catch(error => {
            document.getElementById('result').innerText = '错误: ' + error;
        });
});

// 添加跳转按钮的事件处理器
document.getElementById('redirectBtn').addEventListener('click', () => {
    window.location.href = 'https://www.baidu.com'; // 修改为您想要跳转的 URL
});
