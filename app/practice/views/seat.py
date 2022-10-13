from django.views.generic import TemplateView
from django.shortcuts import render


class Seat(TemplateView):

    # 練習20
    def get(self, request, *args, **kwargs):

        context = {
            'message': '空席があります',
        }
        return render(request, 'practice/seat.html', context)

    def post(self, request):

        seatStr = ''
        message = '空席があります'
        seat = []

        if self.request.POST.get('seat', None):
            seatStr = request.POST['seat']
            if seatStr.count(',') > 0:
                seat = seatStr.split(',')
            else:
                seat.append(seatStr)

        if self.request.POST.get('input_seat', None):
            input_seat = request.POST['input_seat']
            if 0 <= len(seat) < 5:
                seat.append(input_seat)
                seatStr = ','.join(seat)

        if self.request.POST.get('delete_seat', None):
            delete_seat = request.POST['delete_seat']

            if delete_seat in seat:
                seat.remove(delete_seat)
                seatStr = ','.join(seat)

        if len(seat) == 5:
            message = '空席がありません'

        context = {
            'input_seat': '',
            'delete_seat': '',
            'seat': seatStr,
            'message': message,
        }
        return render(request, 'practice/seat.html', context)


seatView = Seat.as_view()
