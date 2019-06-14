from django.shortcuts import render
import telegram # 텔레그램 모듈을 임포트합니다.


def index(request):
    return render(request, 'blog/index.html', {})

def accelerating(request):
    return render(request, 'blog/accelerating.html', {})

def contact(request):
    return render(request, 'blog/contact.html', {})


def listing(request):
    return render(request, 'blog/listing.html', {})

def lp(request):
    return render(request, 'blog/lp.html', {})

def partner(request):
    return render(request, 'blog/partner.html', {})

def portfolio(request):
    return render(request, 'blog/portfolio.html', {})



def post(request):
	if request.method == "POST":
		#print(request.POST['contact_name'])
		my_token = '619219028:AAF_kOpmvY4L3zupsMkPGugS5yxS0lb9HuU' # 토큰을 변수에 저장합니다.
		bot = telegram.Bot(token = my_token) # bot을 선언합니다.
		print(bot.getUpdates())
		
		#updates = bot.getUpdates() # 업데이트 내역을 받아옵니다.
		#for u in updates:
			#print(u.message) # 업데이트 내역 중 메시지를 출력합니다.

		#chat_id = bot.getUpdates()[-1].message.chat.id
		chat_id = 547492157
		#print(chat_id)
		bot.sendMessage(chat_id = chat_id, text='이름 : '+request.POST['contact_name']+'\n이메일 : '+request.POST['contact_email']+'\n내용 :\n'+request.POST['contact_message'])
		return render(request, 'blog/contact.html', {})
	else:
		return render(request, 'blog/contact.html', {})
'''
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit = False)
            lotto.generate()
            return redirect('index')
    else:
        form = PostForm()
        return render(request, "lotto/form.html",{"form": form})
'''