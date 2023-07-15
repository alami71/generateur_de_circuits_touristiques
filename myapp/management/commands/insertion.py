from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from datetime import datetime
from myapp.models import *

class Command(BaseCommand):
    help = 'Inserts Actualite records'

    def handle(self, *args, **options):
        actualite_list = [
            Actualite(id_actu=1, id_circuit=1, titre_actu='Voyage Organisé'),
            Actualite(id_actu=2, id_circuit=2, titre_actu='Voyage Organisé'),
            Actualite(id_actu=3, id_circuit=5, titre_actu='Voyage Organisé'),
        ]
        Actualite.objects.bulk_create(actualite_list)


"""  artisanat_list = [
            Artisanat(id_artisanat=1, nom_artisanat='Tagine', image_artisanat='ARTISANAT-1024x683.jpg', date_modification='2022-05-27 22:54:30'),
            Artisanat(id_artisanat=2, nom_artisanat='Babouche', image_artisanat='Artisanat.jpg', date_modification='2022-05-28 12:08:30'),
            Artisanat(id_artisanat=4, nom_artisanat='Tahrouyt', image_artisanat='tahrouyt.jpg', date_modification='2022-05-28 12:12:37'),
            Artisanat(id_artisanat=5, nom_artisanat='Tapis', image_artisanat='Artisanat-Tapis.jpg', date_modification='2022-05-28 12:13:44'),
        ]
        Artisanat.objects.bulk_create(artisanat_list)

"""
"""         chambre_list = [
            Chambre(num_chambre=1, id_hotel=1, type_chambre='1 personne', prix_chambre='249.00'),
            Chambre(num_chambre=2, id_hotel=1, type_chambre='2 personne', prix_chambre='429.00'),
            Chambre(num_chambre=3, id_hotel=1, type_chambre='familial', prix_chambre='699.00'),
        ]
        Chambre.objects.bulk_create(chambre_list) """


"""         circuit_list = [
            CircuitVoyage(
                id_circuit=1,
                ville_depart='Errachidia',
                ville_arrivee='Zagora',
                trajet='<p>Errachidia -> Arfoud -> Errissani -> Alnif -> Zagora</p>',
                date_depart='2023-07-30 09:00:00',
                duree=3,
                image_cover='ec.jpg',
                image_trajet='<p><iframe style="border: 0;" src="https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d1621793.4860254445!2d-5.561589048506327!3d30.908498026971106!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e0!4m5!1s0xd984a900c95d9db%3A0xe364e4f136aef8b3!2sErrachidia!3m2!1d31.927235999999997!2d-4.4284985!4m5!1s0xdbc36ea58680e95%3A0x75e9e9fb616de232!2sZagora!3m2!1d30.345899799999998!2d-5.8406587!5e0!3m2!1sfr!2sma!4v1653150410027!5m2!1sfr!2sma" width="300px" height="220px" allowfullscreen="allowfullscreen" loading="lazy"></iframe></p>',
                prix='999.99',
                fin_reservation='2023-07-29',
            ),
            CircuitVoyage(
                id_circuit=2,
                ville_depart='Errachidia',
                ville_arrivee='Tinghir',
                trajet='<p>Errachidia -&gt; Goulmima -&gt;Tinejdad -&gt; Tinghir</p>',
                date_depart='2023-07-30 09:00:00',
                duree=2,
                image_cover='arton41819.jpg',
                image_trajet='<p><iframe style=\"border: 0;\" src=\"https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d434572.54242609313!2d-5.261118809415846!3d31.68588908236824!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e0!4m5!1s0xd984a900c95d9db%3A0xe364e4f136aef8b3!2sErrachidia!3m2!1d31.927235999999997!2d-4.4284985!4m5!1s0xdbd332a576e9eb1%3A0x14e34a1d12e39647!2sTinghir!3m2!1d31.5204633!2d-5.5302337!5e0!3m2!1sfr!2sma!4v1653153851400!5m2!1sfr!2sma\" width=\"300\" height=\"220\" allowfullscreen=\"allowfullscreen\" loading=\"lazy\"></iframe></p>',
                prix='999.99',
                fin_reservation='2023-07-29',
            ),
            CircuitVoyage(
                id_circuit=5,
                ville_depart='Tinejdad',
                ville_arrivee='Ouarzazat',
                trajet='<p>Tinejdad -&gt; Tinghir -&gt; Bomalne -&gt; Kl&acirc;at M\'Gouna -&gt;Ouarzazat</p>',
                date_depart='2023-07-24 09:30:00',
                duree=2,
                image_cover='87.jpg',
                image_trajet='<p><iframe src=\"https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d873404.6475114098!2d-6.540975906879432!3d31.228017685156807!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e6!4m5!1s0xd97ffbc8fdf5f09%3A0x7226e3098ee4628!2sTinejdad!3m2!1d31.512853399999997!2d-5.0234472!4m5!1s0xdbb104077422057%3A0x26b3cb529b37ab00!2sOuarzazate!3m2!1d30.9335436!2d-6.937016!5e0!3m2!1sfr!2sma!4v1653731511920!5m2!1sfr!2sma\" width=\"300\" height=\"220\" style=\"border:0;\" allowfullscreen=\"\" loading=\"lazy\" referrerpolicy=\"no-referrer-when-downgrade\"></iframe></p>',
                prix='249.00',
                fin_reservation='2023-07-23',
            ),
            CircuitVoyage(
                id_circuit=7,
                ville_depart='Midelt',
                ville_arrivee='Ouarzazat',
                trajet='<p>Midelt -&gt; Rich -&gt; Errachidia -&gt; Tinghir -&gt; Boumalne Dad&egrave;s -&gt; Kal&acirc;at M\'Gouna -&gt; Ouarzazate</p>',
                date_depart='2023-06-08 10:00:00',
                duree=3,
                image_cover='ouarzazate-hotel-ksarighnda.jpg',
                image_trajet='<iframe src=\"https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d1738596.016019996!2d-6.771387439600543!3d31.66955378460259!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e6!4m5!1s0xd98bf42e8441e9f%3A0x88269ca6a8dbb536!2sMidelt!3m2!1d32.6799423!2d-4.7329267999999995!4m5!1s0xdbb104077422057%3A0x26b3cb529b37ab00!2sOuarzazate!3m2!1d30.9335436!2d-6.937016!5e0!3m2!1sfr!2sma!4v1653732623133!5m2!1sfr!2sma\" width=\"300\" height=\"220\" style=\"border:0;\" allowfullscreen=\"\" loading=\"lazy\" referrerpolicy=\"no-referrer-when-downgrade\"></iframe>',
                prix='1249.00',
                fin_reservation='2023-06-06',
            ),
        ]
        CircuitVoyage.objects.bulk_create(circuit_list)

 """

""" client_list=[
            Client(
                id_client=4,
                nom_client='ZAHIR',
                prenom_client='Ismail',
                email_client='ismailza417@gmail.com',
                login_client='ismail123',
                password_client='b3c55a02882e9050dcd4a6739d4a288c',
                date_inscription=make_aware(datetime(2022, 5, 19, 11, 54, 2)),
                code=0,
                status='verified'
            )
            ]
Client.objects.bulk_create(client_list)
"""
"""  destination_list[
            Destination=(
                id_dest=1,
                nom_dest='Ksar el Khorbat',
                ville_dest='Tinejdad',
                province='Errachidia',
                image_dest1='Ksar-Lkhrbat.jpg',
                image_dest2='27778154258_e02da4c1d0_b.jpg',
                image_dest3='Errachida-Web-106.jpg',
                localisation_dest='https://goo.gl/maps/ug6jMFSaFGpp2efN7',
                carte_dest='<iframe src=\"https://www.google.com/maps/embed?pb=!1m19!1m8!1m3!1d6166.422156578833!2d-5.0897147!3d31.4921771!3m2!1i1024!2i768!4f13.1!4m8!3e6!4m0!4m5!1s0xdbd550e1a32b34d%3A0x4660cf2a4d0b2e08!2sKsar%20Elkhorbat%2C%20Ksar%20Lbour!3m2!1d31.4921725!2d-5.0875259999999995!5e1!3m2!1sfr!2sma!4v1651613652619!5m2!1sfr!2sma\" width=\"400\" height=\"300\" style=\"border:0;\" allowfullscreen=\"\" loading=\"lazy\" referrerpolicy=\"no-referrer-when-downgrade\"></iframe>',
                description_dest='<p><span style=\"font-size: 14pt;\">A 50 km &agrave; l\'est de <span style=\"color: rgb(0, 0, 0);\"><strong>Tinghir </strong></span>(ou <strong>Tinerhir</strong>), dans la basse vall&eacute;e du Todra, El Khorbat est un ancien ksar (village fortifi&eacute;) b&acirc;ti en terre crue au XIX&egrave;me si&egrave;cle et r&eacute;cemment restaur&eacute; gr&acirc;ce &agrave; la coop&eacute;ration internationale.</span></p>\r\n<p><span style=\"font-size: 14pt;\">La moiti&eacute; des maisons d\'El Khorbat sont encore habit&eacute;es. D\'autres ont &eacute;t&eacute; r&eacute;habilit&eacute;es et ont re&ccedil;u une nouvelle fonction : une maison d\'h&ocirc;tes, un mus&eacute;e, un atelier d\'artisanat f&eacute;minin, etc.</span></p>\r\n<p><span style=\"font-size: 14pt;\">L&rsquo;objectif est utiliser l\'&eacute;cotourisme pour sauvegarder un patrimoine historique et artistique d&rsquo;une valeur incalculable : les casbahs en terre crue.</span></p>\r\n<p><span style=\"font-size: 14pt;\">El Khorbat est devenu ainsi le point de d&eacute;part id&eacute;al pour les excursions dans les oasis du Sud marocain, les gorges du Todra et du Gheris'
            )
            ]
        Destination.objects.bulk_create(destination_list)
"""


"""     self.stdout.write(self.style.SUCCESS('Actualite records inserted successfully.'))
"""
""" admin = Admin(
            id_admin=1,
            date_ajout='2022-04-24 23:21:21',
            nom_admin='ZAHIR',
            prenom_admin='Ismail',
            email_admin='ismailza437@gmail.com',
            login_admin='ismailza',
            password_admin='81dc9bdb52d04dc20036dbd8313ed055',
            photo_admin='images/profile/IMG_20210102_203408_124.jpg'
        )
        admin.save() """