import webbrowser


class Score:
    def __init__(self):
        self.score_url = 'http://jwglxt.qau.edu.cn/jsxsd1/kscj/cjcx_list'
        self.data = {
            'kksj': '2019-2020-1',
            'kcxz': '',
            'kcmc': '',
            'xsfs': 'all',
        }

    def replace_css(self, response):
        response = response.replace('/jsxsd1/framework/images/common.css', 'common.css')
        response = response.replace('/jsxsd1/framework/images/blue.css', 'blue.css')
        with open('score.html', 'w', encoding='utf-8') as s_f:
            s_f.write(response)
        webbrowser.open('score.html')