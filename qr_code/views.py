from qr_code.forms import UserCreationForm, LinksForm, UploadFileForm, InteractionNotesForm
from qr_code.models import LinksMetadata, QrcodeImage, InteractionNotes, SecondaryLinksMetadata, LinksDatabaseChoice
from qr_code.serializers import LinksMetadataSerializer, QrcodeImageSerializer, InteractionNotesSerializer, UserSerializer, SecondaryLinksMetadataSerializer, LinksDatabaseChoiceSerializer
from django.shortcuts import render, render_to_response
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.template.context_processors import csrf
from django.forms.models import model_to_dict
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework import viewsets, filters, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from friendship.models import Friend, Follow, Block, FriendshipRequest
from PIL import Image
import qrcode
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

# class SignUp(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'

@csrf_exempt
@api_view(['GET', 'POST'])
def json_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            data = {"status": "success"}
            return JsonResponse(data=data, status=status.HTTP_201_CREATED)
        return JsonResponse(data=form.errors, status=status.HTTP_400_BAD_REQUEST)

def str_to_url(string, type_link):
    if string != "" and string != None:
        if "http" in string or "https" in string:
            return string
        else:
            return "https://" + string

def get_social_links(link_choice, username):
    try:
        user = User.objects.get(username=username)
    except:
        user = ""
    if user != "":
        if link_choice == 1:
            try:
                links = LinksMetadata.objects.get(user=user)
                facebook_link = links.facebook_link
                linkedin_link = links.linkedin_link
                resume_link = links.resume_link
                github_link = links.github_link
                twitter_link = links.twitter_link
                pinterest_link = links.pinterest_link
                portfolio_link = links.portfolio_link
                instagram_link = links.instagram_link
                phone_number = links.phone_number
                email_address = links.email_address
            except:
                facebook_link = ""
                linkedin_link = ""
                resume_link = ""
                github_link = ""
                twitter_link = ""
                pinterest_link = ""
                portfolio_link = ""
                instagram_link = ""
                phone_number = ""
                email_address = ""
        elif link_choice == 2:
            try:
                links = SecondaryLinksMetadata.objects.get(user=user)
                facebook_link = links.facebook_link
                linkedin_link = links.linkedin_link
                resume_link = links.resume_link
                github_link = links.github_link
                twitter_link = links.twitter_link
                pinterest_link = links.pinterest_link
                portfolio_link = links.portfolio_link
                instagram_link = links.instagram_link
                phone_number = links.phone_number
                email_address = links.email_address
            except:
                facebook_link = ""
                linkedin_link = ""
                resume_link = ""
                github_link = ""
                twitter_link = ""
                pinterest_link = ""
                portfolio_link = ""
                instagram_link = ""
                phone_number = ""
                email_address = ""
        else:
            facebook_link = ""
            linkedin_link = ""
            resume_link = ""
            github_link = ""
            twitter_link = ""
            pinterest_link = ""
            portfolio_link = ""
            instagram_link = ""
            phone_number = ""
            email_address = ""
    else:
        facebook_link = ""
        linkedin_link = ""
        resume_link = ""
        github_link = ""
        twitter_link = ""
        pinterest_link = ""
        portfolio_link = ""
        instagram_link = ""
        phone_number = ""
        email_address = ""
    return facebook_link, linkedin_link, resume_link, github_link, twitter_link, pinterest_link, portfolio_link, instagram_link, phone_number, email_address

def post_social_links(link_choice, user, form):
    if link_choice == 1:
        database_check = LinksMetadata.objects.filter(user=user).exists()
        if database_check:
            links = LinksMetadata.objects.get(user=user)
            links.facebook_link = str_to_url(form.cleaned_data['facebook_link'], "facebook")
            links.linkedin_link = str_to_url(form.cleaned_data['linkedin_link'], "linkedin")
            links.resume_link = str_to_url(form.cleaned_data['resume_link'], "resume")
            links.github_link = str_to_url(form.cleaned_data['github_link'], "github")
            links.twitter_link = str_to_url(form.cleaned_data['twitter_link'], "twitter")
            links.pinterest_link = str_to_url(form.cleaned_data['pinterest_link'], "pinterest")
            links.portfolio_link = str_to_url(form.cleaned_data['portfolio_link'], "portfolio")
            links.instagram_link = str_to_url(form.cleaned_data['instagram_link'], "instagram")
            links.phone_number = form.cleaned_data['phone_number']
            links.email_address = form.cleaned_data['email_address']
            links.save()
        else:
            links = LinksMetadata.objects.create(user=user, facebook_link=str_to_url(form.cleaned_data['facebook_link'], "facebook"), linkedin_link=str_to_url(form.cleaned_data['linkedin_link'], "linkedin"), resume_link=str_to_url(form.cleaned_data['resume_link'], "resume"), github_link=str_to_url(form.cleaned_data['github_link'], "github"), twitter_link=str_to_url(form.cleaned_data['twitter_link'], "twitter"), pinterest_link=str_to_url(form.cleaned_data['pinterest_link'], "pinterest"), portfolio_link=str_to_url(form.cleaned_data['portfolio_link'], "portfolio"), instagram_link=str_to_url(form.cleaned_data['instagram_link'], "instagram"), phone_number=form.cleaned_data['phone_number'], email_address=form.cleaned_data['email_address'])
            links.save()
    else:
        database_check = SecondaryLinksMetadata.objects.filter(user=user).exists()
        if database_check:
            links = SecondaryLinksMetadata.objects.get(user=user)
            links.facebook_link = str_to_url(form.cleaned_data['facebook_link'], "facebook")
            links.linkedin_link = str_to_url(form.cleaned_data['linkedin_link'], "linkedin")
            links.resume_link = str_to_url(form.cleaned_data['resume_link'], "resume")
            links.github_link = str_to_url(form.cleaned_data['github_link'], "github")
            links.twitter_link = str_to_url(form.cleaned_data['twitter_link'], "twitter")
            links.pinterest_link = str_to_url(form.cleaned_data['pinterest_link'], "pinterest")
            links.portfolio_link = str_to_url(form.cleaned_data['portfolio_link'], "portfolio")
            links.instagram_link = str_to_url(form.cleaned_data['instagram_link'], "instagram")
            links.phone_number = form.cleaned_data['phone_number']
            links.email_address = form.cleaned_data['email_address']
            links.save()
        else:
            links = SecondaryLinksMetadata.objects.create(user=user, facebook_link=str_to_url(form.cleaned_data['facebook_link'], "facebook"), linkedin_link=str_to_url(form.cleaned_data['linkedin_link'], "linkedin"), resume_link=str_to_url(form.cleaned_data['resume_link'], "resume"), github_link=str_to_url(form.cleaned_data['github_link'], "github"), twitter_link=str_to_url(form.cleaned_data['twitter_link'], "twitter"), pinterest_link=str_to_url(form.cleaned_data['pinterest_link'], "pinterest"), portfolio_link=str_to_url(form.cleaned_data['portfolio_link'], "portfolio"), instagram_link=str_to_url(form.cleaned_data['instagram_link'], "instagram"), phone_number=form.cleaned_data['phone_number'], email_address=form.cleaned_data['email_address'])
            links.save()
    
def index(request, username):
    if request.method == 'GET':
        try:
            user = User.objects.get(username=username)
            link_choice_object = LinksDatabaseChoice.objects.get(user=user)
            link_choice = link_choice_object.links_choice
        except:
            if request.user.is_authenticated and request.user.username == username:
                link_choice_object = LinksDatabaseChoice.objects.create(user=user, links_choice=1)
                link_choice_object.save()
                link_choice = link_choice_object.links_choice
            else:
                link_choice = ""
        facebook_link, linkedin_link, resume_link, github_link, twitter_link, pinterest_link, portfolio_link, instagram_link, phone_number, email_address = get_social_links(link_choice, username)
        try:
            if request.user.is_authenticated and request.user.username != username:
                
                other_user = User.objects.get(username=username)
                if Friend.objects.are_friends(request.user, other_user) == False:
                    try:
                        FriendshipRequest.objects.get(from_user=request.user, to_user=other_user)
                        button_text = ''
                        try:
                            other_user = User.objects.get(username=username)
                            interaction_notes = InteractionNotes.objects.get(other_user=other_user, user=request.user)
                            data = {'interaction_notes': interaction_notes.interaction_notes}
                            interactionnotes_form = InteractionNotesForm(initial=data)
                        except:
                            interactionnotes_form = InteractionNotesForm()
                    except:
                        button_text = 'Add Connection'
                        interactionnotes_form = ''
                else:
                    button_text = ''
                    try:
                        other_user = User.objects.get(username=username)
                        interaction_notes = InteractionNotes.objects.get(other_user=other_user, user=request.user)
                        data = {'interaction_notes': interaction_notes.interaction_notes}
                        interactionnotes_form = InteractionNotesForm(initial=data)
                    except:
                        interactionnotes_form = InteractionNotesForm()
            else:
                button_text = ''
                interactionnotes_form = ''
        except:
            button_text = ''
            interactionnotes_form = ''
        return render(request, 'home.html', {'username': username, 'facebook_link': facebook_link, 'linkedin_link': linkedin_link, 'resume_link': resume_link, 'github_link': github_link, 'twitter_link': twitter_link, 'pinterest_link': pinterest_link, 'portfolio_link': portfolio_link, 'instagram_link': instagram_link, 'phone_number': phone_number, 'link_choice': link_choice, 'interactionnotes_form': interactionnotes_form, 'button_text': button_text, 'email_address': email_address})
    else:
        other_user = User.objects.get(username=username)
        if 'add-contact' in request.POST:
            try:
                Friend.objects.add_friend(request.user, other_user)
                button_text = '✓ Connection Request Sent'
                link_choice_object = LinksDatabaseChoice.objects.get(user=other_user)
                link_choice = link_choice_object.links_choice
                facebook_link, linkedin_link, resume_link, github_link, twitter_link, pinterest_link, portfolio_link, instagram_link, phone_number, email_address = get_social_links(link_choice, other_user.username)
            except:
                button_text = '✓ Connection Request Already Sent'
                link_choice_object = LinksDatabaseChoice.objects.get(user=other_user)
                link_choice = link_choice_object.links_choice
                facebook_link, linkedin_link, resume_link, github_link, twitter_link, pinterest_link, portfolio_link, instagram_link, phone_number, email_address = get_social_links(link_choice, other_user.username)
            try:
                interaction_notes = InteractionNotes.objects.get(other_user=other_user, user=request.user)
                data = {'interaction_notes': interaction_notes.interaction_notes}
                interactionnotes_form = InteractionNotesForm(initial=data)
            except:
                interactionnotes_form = InteractionNotesForm()
        elif 'change-profile' in request.POST:
            link_choice_object = LinksDatabaseChoice.objects.get(user=request.user)
            if link_choice_object.links_choice == 1:
                link_choice_object.links_choice = 2
                link_choice_object.save()
            elif link_choice_object.links_choice == 2:
                link_choice_object.links_choice = 1
                link_choice_object.save()
            button_text = ''
            interactionnotes_form = ''
            link_choice_object = LinksDatabaseChoice.objects.get(user=request.user)
            link_choice = link_choice_object.links_choice
            facebook_link, linkedin_link, resume_link, github_link, twitter_link, pinterest_link, portfolio_link, instagram_link, phone_number, email_address = get_social_links(link_choice, request.user.username)
        elif 'interaction-notes' in request.POST:
            interactionnotes_form = InteractionNotesForm(request.POST)
            if interactionnotes_form.is_valid():
                database_check = InteractionNotes.objects.filter(user=request.user, other_user=other_user).exists()
                if database_check:
                    interaction_notes = InteractionNotes.objects.get(other_user=other_user.username, user=request.user)
                    interaction_notes.interaction_notes = interactionnotes_form.cleaned_data['interaction_notes']
                    interaction_notes.save()
                else:
                    interaction_notes = InteractionNotes.objects.create(user=request.user, other_user=other_user.username, interaction_notes=interactionnotes_form.cleaned_data['interaction_notes'])
                    interaction_notes.save()
            button_text = ''
            try:
                link_choice_object = LinksDatabaseChoice.objects.get(user=other_user)
                link_choice = link_choice_object.links_choice
                facebook_link, linkedin_link, resume_link, github_link, twitter_link, pinterest_link, portfolio_link, instagram_link, phone_number, email_address = get_social_links(link_choice, username)
            except:
                link_choice = ''
                facebook_link, linkedin_link, resume_link, github_link, twitter_link, pinterest_link, portfolio_link, instagram_link, phone_number, email_address = get_social_links('', username)
        return render(request, 'home.html', {'username': username, 'facebook_link': facebook_link, 'linkedin_link': linkedin_link, 'resume_link': resume_link, 'github_link': github_link, 'twitter_link': twitter_link, 'pinterest_link': pinterest_link, 'portfolio_link': portfolio_link, 'instagram_link': instagram_link, 'phone_number': phone_number, 'button_text': button_text, 'link_choice': link_choice, 'interactionnotes_form': interactionnotes_form, 'email_address': email_address})

def links_form(request):
    link_choice = int(request.GET.get('profile', '1'))
    if link_choice != 1 and link_choice != 2:
        link_choice = 1
    if request.method == 'GET':
        try:
            user = User.objects.get(username=request.user.username)
            # link_choice_object = LinksDatabaseChoice.objects.get(user=user)
            # link_choice = link_choice_object.links_choice
            facebook_link, linkedin_link, resume_link, github_link, twitter_link, pinterest_link, portfolio_link, instagram_link, phone_number, email_address = get_social_links(link_choice, user.username)
            data = {'facebook_link': facebook_link, 'linkedin_link': linkedin_link, 'resume_link': resume_link, 'github_link': github_link, 'twitter_link': twitter_link, 'pinterest_link': pinterest_link, 'portfolio_link': portfolio_link, 'instagram_link': instagram_link, 'phone_number': phone_number, 'email_address': email_address}
            form = LinksForm(initial=data)
        except:
            form = LinksForm()
            links = ""
    else:
        form = LinksForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            # link_choice_object = LinksDatabaseChoice.objects.get(user=user)
            # link_choice = link_choice_object.links_choice
            post_social_links(link_choice, user, form)
            url = "/users/" + user.username
            return HttpResponseRedirect(url)
    return render(request, 'linksfields.html', {'form': form})

def navigation_guide(request):
    if request.method == "GET":
        user = User.objects.get(username=request.user.username)
        return render(request, 'navigationguide.html', {'user': user})

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            subject, from_email, to = 'Thank you for signing up with SMESH!', 'SMESH <hellosmesh@gmail.com>', form.cleaned_data.get('email')
            html_content = render_to_string("react_email_template.html", {
                "first_name": form.cleaned_data.get('first_name'),
            })
            text_content = "Please enable the use of HTML for this email."
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password2')
            user = authenticate(username=username, password=password)
            login(request, user)
            # user = User.objects.get(username=form.cleaned_data['username'])
            # links_entry = LinksDatabaseChoice.objects.create(user=user)
            # links_entry.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
    # args = {}
    # args.update(csrf(request))
    # args['form'] = UserCreationForm()
    # return render_to_response('signup.html', args)

def generate_qrcode(request):
    if request.method == 'GET':
        user = User.objects.get(username=request.user.username)
        try:
            qrcode_link = QrcodeImage.objects.get(user=user).image.url
        except:
            qrcode_link = None
        form = UploadFileForm()
        return render(request, 'generate_qrcode.html', {'form': form, 'qrcode_link': qrcode_link})
    else:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            im = Image.open(request.FILES['image'])
            im = im.convert('RGB')
            user = User.objects.get(username=request.user.username)
            url = request.build_absolute_uri('/users/' + user.username)
            database_check = QrcodeImage.objects.filter(user=user).exists()
            if database_check:
                qrcodeim = QrcodeImage.objects.get(user=user)
                img_width, img_height = im.size
                qrcode_img = qrcode.make(url)
                qr_width, qr_height = qrcode_img.size
                # Resize QR code to 20% of image
                resized_qr_width = 0.2 * img_width
                qrcode_img = qrcode_img.resize((int(resized_qr_width), int(resized_qr_width)))
                # Paste QR code on bottom centre of image
                im.paste(qrcode_img, (int((img_width - resized_qr_width) / 2), int(img_height - resized_qr_width)))
                stringio_obj = BytesIO()
                im.save(stringio_obj, format="JPEG")
                request.FILES['image'] = InMemoryUploadedFile(stringio_obj, 
                    None, "{}.jpg".format(user.username), 'image/jpeg',
                    stringio_obj.getbuffer().nbytes, None)
                qrcodeim.image = request.FILES['image']
                qrcodeim.save()
            else:
                img_width, img_height = im.size
                qrcode_img = qrcode.make(url)
                qr_width, qr_height = qrcode_img.size
                # Resize QR code to 20% of image
                resized_qr_width = 0.2 * img_width
                qrcode_img = qrcode_img.resize((int(resized_qr_width), int(resized_qr_width)))
                # Paste QR code on bottom centre of image
                im.paste(qrcode_img, (int((img_width - resized_qr_width) / 2), int(img_height - resized_qr_width)))
                stringio_obj = BytesIO()
                im.save(stringio_obj, format="JPEG")
                request.FILES['image'] = InMemoryUploadedFile(stringio_obj, 
                    None, "{}.jpg".format(user.username), 'image/jpeg',
                    stringio_obj.getbuffer().nbytes, None)
                qrcodeim = QrcodeImage.objects.create(user=request.user, image=request.FILES['image']) 
                qrcodeim.save()
            return HttpResponseRedirect(qrcodeim.image.url)
        else:
            return HttpResponseBadRequest()

def all_friends(request):
    if request.method == 'GET':
        all_friends = Friend.objects.friends(request.user)
        urls = [("/users/" + user.username, "/interaction-notes/" + user.username, user) for user in all_friends]
        return render(request, 'allfriends.html', {'friends': urls})

def friends_management(request):
    if request.method == 'GET':
        received_connections = Friend.objects.unrejected_requests(user=request.user)
        sent_connections = Friend.objects.sent_requests(user=request.user)
        return render(request, 'friends_management.html', {'received_connections': received_connections, 'sent_connections': sent_connections})
    else:
        friend_request = FriendshipRequest.objects.get(from_user=User.objects.get(username=request.POST["from_user"]), to_user=request.user)
        friend_request.accept()
        received_connections = Friend.objects.unrejected_requests(user=request.user)
        sent_connections = Friend.objects.sent_requests(user=request.user)
        return render(request, 'friends_management.html', {'received_connections': received_connections, 'sent_connections': sent_connections})

def interaction_notes(request, username):
    if request.method == 'GET':
        try:
            other_user = User.objects.get(username=username)
            if Friend.objects.are_friends(request.user, other_user) == False:
                other_user = ""
        except:
            other_user = ""
        try:
            interaction_notes = InteractionNotes.objects.get(other_user=other_user, user=request.user)
            data = {'interaction_notes': interaction_notes.interaction_notes}
            form = InteractionNotesForm(initial=data)
        except:
            form = InteractionNotesForm()
        return render(request, 'interactionnotes.html', {'form': form, 'username': other_user})
    else:
        form = InteractionNotesForm(request.POST)
        if form.is_valid():
            other_user = User.objects.get(username=username)
            database_check = InteractionNotes.objects.filter(user=request.user).exists()
            if database_check:
                interaction_notes = InteractionNotes.objects.get(other_user=other_user.username, user=request.user)
                interaction_notes.interaction_notes = form.cleaned_data['interaction_notes']
                interaction_notes.save()
            else:
                interaction_notes = InteractionNotes.objects.create(user=request.user, other_user=other_user.username, interaction_notes=form.cleaned_data['interaction_notes'])
                interaction_notes.save()
        return render(request, 'interactionnotes.html', {'form': form, 'username': other_user})

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('username', 'email')

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        if (self.request.user.is_superuser):
            return User.objects.all()
        else:
            return User.objects.filter(is_staff=False, is_superuser=False, username=user.username)

class UserDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = UserSerializer(profile, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = UserSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LinksMetadataView(viewsets.ModelViewSet):
    queryset = LinksMetadata.objects.all()
    serializer_class = LinksMetadataSerializer
    permission_classes = (IsAdminUser,)
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('user', 'lastUpdatedTime')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LinksMetadataDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return LinksMetadata.objects.get(pk=pk)
        except LinksMetadata.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = LinksMetadataSerializer(profile, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = LinksMetadataSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SecondaryLinksMetadataView(viewsets.ModelViewSet):
    queryset = SecondaryLinksMetadata.objects.all()
    serializer_class = SecondaryLinksMetadataSerializer
    permission_classes = (IsAdminUser,)
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('user', 'lastUpdatedTime')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SecondaryLinksMetadataDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return SecondaryLinksMetadata.objects.get(pk=pk)
        except SecondaryLinksMetadata.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = SecondaryLinksMetadataSerializer(profile, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = SecondaryLinksMetadataSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class QrcodeImageView(viewsets.ModelViewSet):
    queryset = QrcodeImage.objects.all()
    serializer_class = QrcodeImageSerializer
    permission_classes = (IsAdminUser,)
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('user', 'lastUpdatedTime')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class QrcodeImageDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return QrcodeImage.objects.get(pk=pk)
        except QrcodeImage.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = QrcodeImageSerializer(profile, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = QrcodeImageSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class InteractionNotesView(viewsets.ModelViewSet):
    queryset = InteractionNotes.objects.all()
    serializer_class = InteractionNotesSerializer
    permission_classes = (IsAdminUser,)
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('user', 'other_user', 'lastUpdatedTime')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class InteractionNotesDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return InteractionNotes.objects.get(pk=pk)
        except InteractionNotes.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = InteractionNotesSerializer(profile, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = InteractionNotesSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LinksDatabaseChoiceView(viewsets.ModelViewSet):
    queryset = LinksDatabaseChoice.objects.all()
    serializer_class = LinksDatabaseChoiceSerializer
    permission_classes = (IsAdminUser,)
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('user', 'links_choice', 'lastUpdatedTime')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LinksDatabaseChoiceDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return LinksDatabaseChoice.objects.get(pk=pk)
        except LinksDatabaseChoice.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = LinksDatabaseChoiceSerializer(profile, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = LinksDatabaseChoiceSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)