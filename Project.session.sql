INSERT INTO public.app_hotel_chain(
	chain_id, 'addressArray', name, email, 'nTelephones', rating, image_url, 'numberOfHotels')
	VALUES (1, Array['293 Mich St, Ottawa, ON'], 'Hotels Mich', 'uottawa@hotelskhouri.com', Array[613-432-1234], 4, 'https://i.pinimg.com/736x/2d/fa/29/2dfa29a9762b4fba3a7ed60c227e4517.jpg', 8),
           (2, Array['435 Kevin Ave, Toronto, ON'], 'Hotels Tawardos', 'uottawa@hotelstawadros.com', Array[647-344-4213], 5, 'https://previews.123rf.com/images/pixbold/pixbold2104/pixbold210400058/166908130-rw-logo-design-vector-swoosh-letter-rw-logo-design.jpg', 8),
           (3, Array['721 Emiliano Rd, Montreal, QC'], 'Hotels Guad', 'uottawa@hotelsguad.com', Array[418-532-0987], 5, 'https://www.logolynx.com/images/logolynx/5d/5d1dc02726b02c08ffd4e4f7bbe5e022.jpeg', 8),
           (4, Array['777 Rod St Vancouver, BC'], 'Hotels Wave', 'uottawa@hotelswave.com', Array[604-738-2034], 4, 'https://static.vecteezy.com/system/resources/previews/007/725/885/original/alphabet-letters-initials-monogram-logo-kt-tk-k-and-t-free-vector.jpg', 8),
           (5, Array['069 Rottweiler St, Halifax, NS'], 'Hotels Loki','uottawa@hotelsloki.com', Array[902-420-8989], 3, 'https://static.vecteezy.com/system/resources/previews/007/932/452/original/letter-hk-logo-design-vector.jpg', 8); 





INSERT INTO public.app_hotel(
	hotel_id, address, zone, name, 'nTelephone', email, rating, image_url, chain_id_id, numberOfRooms)
	VALUES (011, '120 MacLaren St', 'Ottawa, Ontario', 'Residence Inn par Hotelskhouri', Array['613-444-1111'], 'uottawa@residenceinn.ca', 2, 'https://st2.depositphotos.com/4035913/8096/i/600/depositphotos_80964546-stock-photo-bucharest-at-sunset.jpg', 1, 5),
    (012, '240 Carling Ave', 'Ottawa, Ontario', 'Courtyard par Hotelskhouri', Array['613-222-7575'], 'uottawa@courtyard.ca', 5, 'https://www.re-thinkingthefuture.com/wp-content/uploads/2020/08/A1609-10-things-to-remember-while-designing-hotels.jpg', 1, 5),
    (013, '534 Bank Ave', 'Ottawa, Ontario', 'Delta par Hotelskhouri', Array['613-560-3200'], 'uottawa@delta.ca', 3, 'https://media.istockphoto.com/id/187363337/photo/modern-hotel-building-in-summer.jpg?s=612x612&w=0&k=20&c=eRVDcadZTKs5t2K-CEeXT6DiJQ68Fnbs6u9F-0S_v8Q=', 1, 5),
    (014, '149 Dixie Dr', 'Ottawa, Ontario', 'Fairfield par Hotelskhouri', Array['613-893-4026'], 'uottawa@fairfield.ca', 3, 'https://insights.ehotelier.com/wp-content/uploads/sites/6/2023/01/Screen-Shot-2023-01-18-at-9.13.28-pm-768x388.png', 1, 5),
    (015, '102 Billings Ave', 'Ottawa, Ontario', 'TownePlace par Hotelskhouri', Array['613-985-7140'], 'uottawa@towneplace.ca', 5, 'https://images.thestar.com/vBk6TJ-OgECrGRuJ4pYCAdaxj_E=/1280x1024/smart/filters:cb(1569967813517)/https://www.thestar.com/content/dam/thestar/halifax/2019/07/25/very-high-end-12-storey-hotel-approved-for-downtown-halifax/a_hal_steele_hotel25.jpg', 1, 5),
    (016, '993 Drive Rd', 'Ottawa, Ontario', 'Fourpoints par Hotelskhouri', Array['613-552-9588'], 'uottawa@fourpoints.ca', 5, 'https://static1.gensler.com/uploads/image/79774/01_project-walt-disney-world-swan-reserve-hotel-01-2000x1125_1651275624_1024x576_1672965528.jpg', 1, 5),
    (017, '457 Guerth Ave', 'Ottawa, Ontario', 'Westin par Hotelskhouri', Array['613-553-7217'], 'uottawa@westin.ca', 4, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSx72CiljttwL_eOFk79qeieiSDnMd4_Rjmgw&usqp=CAU', 1, 5),
    (018, '604 Bryce Ave', 'Ottawa, Ontario', 'Sheraton par Hotelskhouri', Array['613-764-2321'], 'uottawa@sheraton.ca', 2, 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/18/0e/ce/a0/le-magnifique-hotel-de.jpg?w=1200&h=1200&s=1', 1, 5),
	(021, '136 Ferrari St', 'Toronto, Ontario', 'Best West par Hotelstawadros', Array['647-444-1111'], 'uottawa@bestwest.ca', 3, 'https://upload.wikimedia.org/wikipedia/commons/3/37/Delta_Hotel.jpg', 2, 5),
    (022, '650 Harry Ave', 'Toronto, Ontario', 'Holiday Inn par Hotelstawadros', Array['647-222-7575'], 'uottawa@holiday.ca', 5, 'https://digital.ihg.com/is/image/ihg/intercontinental-toronto-4084375988-4x3', 2, 5),
    (023, '932 Peter St', 'Toronto, Ontario', 'Radisson par Hotelstawadros', Array['647-783-3972'], 'uottawa@radisson.ca', 3, 'https://www.reminetwork.com/wp-content/uploads/hotel-x-toronto.jpg', 2, 5),
    (024, '800 Basil Rd', 'Toronto, Ontario', 'Novotel par Hotelstawadros', Array['647-082-5126'], 'uottawa@novotel.ca', 5, 'https://www.gouverneur.com/uploads/1/0/6/8/106825145/published/gouvernement-provincial-hiver_3.jpg?1576850606', 2, 5),
    (025, '637 Apple St', 'Toronto, Ontario', 'Trinity par Hotelstawadros', Array['647-785-5000'], 'uottawa@trinity.ca', 4, 'https://media-cms.vrbo.com//images/gxwgulxyxxy1/70kJsxr01x9klZh6E4oFdT/e454a9f9ee08b2b042000fd5c590ee9d/0_200419149-001.jpg?impolicy=resizecrop&rw=1024&rh=429&ch=429&cw=1024&ra=fill&q=mediumHigh', 2, 5),
    (026, '993 Saints Ave', 'Toronto, Ontario', 'Fairmont par Hotelstawadros', Array['647-899-0010'], 'uottawa@fairmont.ca', 3, 'https://phgcdn.com/images/uploads/YQBLC/masthead/1600x813-Exterior-2-Fairmont-le-Chateau-Montebello-Quebec-Canada.jpg', 2, 5),
    (027, '632 Cosmic Ave', 'Toronto, Ontario', 'King par Hotelstawadros', Array['647-746-4764'], 'uottawa@king.ca', 5, 'https://www.telegraph.co.uk/content/dam/Travel/hotels/2022/march/the-langdale-hotel-lake-district-p.jpg', 2, 5),
    (028, '604 Hunter Ave', 'Toronto, Ontario', 'Chelsea par Hotelstawadros', Array['647-904-2211'], 'uottawa@chelsea.ca', 3, 'https://media-cdn.tripadvisor.com/media/photo-s/18/2a/3b/f8/in-the-middle-of-the.jpg', 2, 5), 
	(031, '989 Fountain St', 'Montreal, Quebec', 'Hilton par Hotelsguad', Array['418-444-1111'], 'uottawa@hilton.ca', 4, 'https://images.charmingsardinia.com/hotels/1077/static/files/bio-hotel-hermitage01.jpg', 3, 5),
    (032, '554 Middle Ave', 'Montreal, Quebec', 'Universel par Hotelsguad', Array['418-222-7575'], 'uottawa@universel.ca', 4, 'https://www.fodors.com/wp-content/uploads/2017/10/mnt8.jpg', 3, 5),
    (033, '713 Oval St', ', Montreal, Quebec', 'Lofts par Hotelsguad', Array['418-783-3972'], 'uottawa@lofts.ca', 4, 'https://www.planetware.com/wpimages/2019/04/canada-quebec-quebec-city-best-hotels-auberge-saint-antoine.jpg', 3, 5),
    (034, '934 Bacon Rd', 'Montreal, Quebec', 'Concorde par Hotelsguad', Array['418-082-5126'], 'uottawa@concorde.ca', 5, 'https://www.gouverneur.com/uploads/1/0/6/8/106825145/published/gouvernement-provincial-hiver_3.jpg?1576850606', 3, 5),
    (035, '712 Maple St', 'Montreal, Quebec', 'Jardin par Hotelsguad', Array['418-785-5000'], 'uottawa@jardin.ca', 4, 'https://media-cms.vrbo.com//images/gxwgulxyxxy1/70kJsxr01x9klZh6E4oFdT/e454a9f9ee08b2b042000fd5c590ee9d/0_200419149-001.jpg?impolicy=resizecrop&rw=1024&rh=429&ch=429&cw=1024&ra=fill&q=mediumHigh', 3, 5),
    (036, '521 Anchor Ave', 'Montreal, Quebec', 'Quartier par Hotelsguad', Array['418-899-0010'], 'uottawa@quartier.ca', 3, 'https://phgcdn.com/images/uploads/YQBLC/masthead/1600x813-Exterior-2-Fairmont-le-Chateau-Montebello-Quebec-Canada.jpg', 3, 5),
    (037, '549 Chestnut Ave', 'Montreal, Quebec', 'Travelodge par Hotelsguad', Array['418-746-4764'], 'uottawa@travelodge.ca', 2, 'https://www.telegraph.co.uk/content/dam/Travel/hotels/2022/march/the-langdale-hotel-lake-district-p.jpg', 3, 5),
    (038, '741 Arctic Ave', 'Montreal, Quebec', 'Repotel par Hotelsguad', Array['418-904-2211'], 'uottawa@repotel.ca', 5, 'https://media-cdn.tripadvisor.com/media/photo-s/18/2a/3b/f8/in-the-middle-of-the.jpg', 3, 5), 
	(041, '831 Draven St', 'Vancouver, British Columbia', 'Element par Hotelswave', Array['604-444-1111'], 'uottawa@element.ca', 4, 'https://upload.wikimedia.org/wikipedia/commons/a/a9/Hotel_vanc_2007.jpg', 4, 5),
	(042, '622 Knight Ave', 'Vancouver, British Columbia', 'Panpacif par Hotelswave', Array['604-222-7575'], 'uottawa@panpacif.ca', 2, 'https://www.traveller.com.au/content/dam/images/g/m/7/x/p/f/image.gallery.galleryLandscape.620x414.gmakjr.png/1453333612558.jpg', 4, 5),
	(043, '482 Petal St', 'Vancouver, British Columbia', 'Marpole par Hotelswave', Array['604-783-3972'], 'uottawa@marpole.ca', 4, 'https://content.r9cdn.net/rimg/himg/c4/a0/5e/ice-32483-102819633-191720.jpg?width=440&height=220&crop=true', 4, 5),
	(044, '903 Garnet Rd', 'Vancouver, British Columbia', 'Executive par Hotelswave', Array['604-082-5126'], 'uottawa@executive.ca', 4, 'https://storeys.com/wp-content/uploads/2023/03/Marcon-W-Pender-Richards-Street-Downtown-Vancouver-Hotel-1.jpg', 4, 5),
	(045, '510 Shorten St', 'Vancouver, British Columbia', 'Sutton par Hotelswave', Array['604-785-5000'], 'uottawa@sutton.ca', 5, 'https://cf.bstatic.com/xdata/images/hotel/270x200/88496364.jpg?k=fc4daae0b1c02c9e1177f67ec789ab88980155c598342fe8487291a791c590d8&o=', 4, 5),
	(046, '614 Kream Ave', 'Vancouver, British Columbia', 'River par Hotelswave', Array['604-899-0010'], 'uottawa@river.ca', 3, 'https://media-magazine.trivago.com/wp-content/uploads/2018/08/29080558/hotel-blu-vancouver.jpeg', 4, 5),
	(047, '741 Park Ave', 'Vancouver, British Columbia', 'Darius par Hotelswave', Array['604-746-4764'], 'uottawa@darius.ca', 5, 'https://media.hrs.com/media/image/05/3e/e1/Four_Seasons_Hotel_Vancouver-Vancouver-Aussenansicht-1-33285_1280x1280.jpg', 4, 5),
	(048, '852 Beaux Ave', 'Vancouver, British Columbia', 'Morgana par Hotelswave', Array['604-844-6667'], 'uottawa@morgana.ca', 3, 'https://ik.imgkit.net/3vlqs5axxjf/external/ik-seo/http://images.ntmllc.com/v4/hotel/P94/P94601/P94601_EXT_ZB34FD/910-Beach-Ave-Apartment-Hotel-Exterior.jpg?tr=w-780%2Ch-437%2Cfo-auto', 4, 5), 
	(051, '314 Riven St', 'Halifax, Nova Scotia', 'Malphite par Hotelswave', Array['902-543-1400'], 'uottawa@malphite.ca', 3, 'https://www.novascotia.com/sites/default/files/2019-05/Quarterdeck%20Resort%20Villas%201920x1080.jpg', 5, 5),
	(052, '105 Jade Ave', 'Halifax, Nova Scotia', 'Marriott par Hotelswave', Array['902-111-3995'], 'uottawa@marriott.ca', 4, 'https://cdn.budgetyourtrip.com/images/photos/headerphotos/medium/canada_halifax.jpg', 5, 5),
	(053, '639 Church St', 'Halifax, Nova Scotia', 'Mundo par Hotelswave', Array['902-888-9979'], 'uottawa@mundo.ca', 5, 'https://static.wixstatic.com/media/3aafcb_9f55001595ee4e22b63a0c6a3264edb8~mv2.jpg/v1/fill/w_640,h_426,al_l,q_80,usm_0.66_1.00_0.01,enc_auto/3aafcb_9f55001595ee4e22b63a0c6a3264edb8~mv2.jpg', 5, 5),
	(054, '834 Rose Rd', 'Halifax, Nova Scotia', 'Sigma par Hotelswave', Array['902-002-5146'], 'uottawa@sigma.ca', 3, 'https://i0.wp.com/files.tripstodiscover.com/files/2015/05/White-Point-Beach-Resort.jpg?resize=784%2C588', 5, 5),
	(055, '128 Trinity St', 'Halifax, Nova Scotia', 'Delta par Hotelswave', Array['902-178-4343'], 'uottawa@delta.ca', 5, 'https://www.whitepoint.com/content/uploads/2022/12/WhitePointBbeachResortatsunset-1920x898.jpg', 5, 5),
	(056, '843 Manor Ave', 'Halifax, Nova Scotia', 'Winston par Hotelswave', Array['902-624-1545'], 'uottawa@winston.ca', 4, 'https://content.r9cdn.net/himg/7a/39/4c/leonardo-31779-150589310-299499.jpg', 5, 5),
	(057, '731 Mount Ave', 'Halifax, Nova Scotia', 'McCree par Hotelswave', Array['902-746-4565'], 'uottawa@mccree.ca', 3, 'https://www.ca.kayak.com/rimg/himg/20/39/cb/leonardo-1053285-hotel_O-295650.jpg?width=1366&height=768&xhint=1320&yhint=829&crop=true', 5, 5),
	(058, '475 Silver Ave', 'Halifax, Nova Scotia', 'Lucio par Hotelswave', Array['902-355-8632'], 'uottawa@lucio.ca', 2, 'https://www.choicehotels.com/hotelmedia/CA/NS/halifax/CN207/320/CN207Exterior06_1.jpg', 5, 5);






INSERT INTO public.app_hotel_chain(
	chain_id, "addressArray", name, email, "nTelephones", rating, image_url, "numberOfHotels")
	VALUES (1, Array['293 Mich St, Ottawa, ON'], 'Hotels Mich', 'uottawa@hotelskhouri.com', Array[613-432-1234], 4, 'https://i.pinimg.com/736x/2d/fa/29/2dfa29a9762b4fba3a7ed60c227e4517.jpg', 8),
           (2, Array['435 Kevin Ave, Toronto, ON'], 'Hotels Tawardos', 'uottawa@hotelstawadros.com', Array[647-344-4213], 5, 'https://previews.123rf.com/images/pixbold/pixbold2104/pixbold210400058/166908130-rw-logo-design-vector-swoosh-letter-rw-logo-design.jpg', 8),
           (3, Array['721 Emiliano Rd, Montreal, QC'], 'Hotels Guad', 'uottawa@hotelsguad.com', Array[418-532-0987], 5, 'https://www.logolynx.com/images/logolynx/5d/5d1dc02726b02c08ffd4e4f7bbe5e022.jpeg', 8),
           (4, Array['777 Rod St Vancouver, BC'], 'Hotels Wave', 'uottawa@hotelswave.com', Array[604-738-2034], 4, 'https://static.vecteezy.com/system/resources/previews/007/725/885/original/alphabet-letters-initials-monogram-logo-kt-tk-k-and-t-free-vector.jpg', 8),
           (5, Array['069 Rottweiler St, Halifax, NS'], 'Hotels Loki','uottawa@hotelsloki.com', Array[902-420-8989], 3, 'https://static.vecteezy.com/system/resources/previews/007/932/452/original/letter-hk-logo-design-vector.jpg', 8);
;
INSERT INTO public.app_hotel(
	hotel_id, address, zone, name, "nTelephones", email, rating, image_url, chain_id_id, numberOfRooms)
	VALUES (011, '120 MacLaren St', 'Ottawa, Ontario', 'Residence Inn par Hotelskhouri', Array['613-444-1111'], 'uottawa@residenceinn.ca', 2, 'https://st2.depositphotos.com/4035913/8096/i/600/depositphotos_80964546-stock-photo-bucharest-at-sunset.jpg', 1, 5),
    (012, '240 Carling Ave', 'Ottawa, Ontario', 'Courtyard par Hotelskhouri', Array['613-222-7575'], 'uottawa@courtyard.ca', 5, 'https://www.re-thinkingthefuture.com/wp-content/uploads/2020/08/A1609-10-things-to-remember-while-designing-hotels.jpg', 1, 5),
    (013, '534 Bank Ave', 'Ottawa, Ontario', 'Delta par Hotelskhouri', Array['613-560-3200'], 'uottawa@delta.ca', 3, 'https://media.istockphoto.com/id/187363337/photo/modern-hotel-building-in-summer.jpg?s=612x612&w=0&k=20&c=eRVDcadZTKs5t2K-CEeXT6DiJQ68Fnbs6u9F-0S_v8Q=', 1, 5),
    (014, '149 Dixie Dr', 'Ottawa, Ontario', 'Fairfield par Hotelskhouri', Array['613-893-4026'], 'uottawa@fairfield.ca', 3, 'https://insights.ehotelier.com/wp-content/uploads/sites/6/2023/01/Screen-Shot-2023-01-18-at-9.13.28-pm-768x388.png', 1, 5),
    (015, '102 Billings Ave', 'Ottawa, Ontario', 'TownePlace par Hotelskhouri', Array['613-985-7140'], 'uottawa@towneplace.ca', 5, 'https://images.thestar.com/vBk6TJ-OgECrGRuJ4pYCAdaxj_E=/1280x1024/smart/filters:cb(1569967813517)/https://www.thestar.com/content/dam/thestar/halifax/2019/07/25/very-high-end-12-storey-hotel-approved-for-downtown-halifax/a_hal_steele_hotel25.jpg', 1, 5),
    (016, '993 Drive Rd', 'Ottawa, Ontario', 'Fourpoints par Hotelskhouri', Array['613-552-9588'], 'uottawa@fourpoints.ca', 5, 'https://static1.gensler.com/uploads/image/79774/01_project-walt-disney-world-swan-reserve-hotel-01-2000x1125_1651275624_1024x576_1672965528.jpg', 1, 5),
    (017, '457 Guerth Ave', 'Ottawa, Ontario', 'Westin par Hotelskhouri', Array['613-553-7217'], 'uottawa@westin.ca', 4, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSx72CiljttwL_eOFk79qeieiSDnMd4_Rjmgw&usqp=CAU', 1, 5),
    (018, '604 Bryce Ave', 'Ottawa, Ontario', 'Sheraton par Hotelskhouri', Array['613-764-2321'], 'uottawa@sheraton.ca', 2, 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/18/0e/ce/a0/le-magnifique-hotel-de.jpg?w=1200&h=1200&s=1', 1, 5),
	(021, '136 Ferrari St', 'Toronto, Ontario', 'Best West par Hotelstawadros', Array['647-444-1111'], 'uottawa@bestwest.ca', 3, 'https://upload.wikimedia.org/wikipedia/commons/3/37/Delta_Hotel.jpg', 2, 5),
    (022, '650 Harry Ave', 'Toronto, Ontario', 'Holiday Inn par Hotelstawadros', Array['647-222-7575'], 'uottawa@holiday.ca', 5, 'https://digital.ihg.com/is/image/ihg/intercontinental-toronto-4084375988-4x3', 2, 5),
    (023, '932 Peter St', 'Toronto, Ontario', 'Radisson par Hotelstawadros', Array['647-783-3972'], 'uottawa@radisson.ca', 3, 'https://www.reminetwork.com/wp-content/uploads/hotel-x-toronto.jpg', 2, 5),
    (024, '800 Basil Rd', 'Toronto, Ontario', 'Novotel par Hotelstawadros', Array['647-082-5126'], 'uottawa@novotel.ca', 5, 'https://www.gouverneur.com/uploads/1/0/6/8/106825145/published/gouvernement-provincial-hiver_3.jpg?1576850606', 2, 5),
    (025, '637 Apple St', 'Toronto, Ontario', 'Trinity par Hotelstawadros', Array['647-785-5000'], 'uottawa@trinity.ca', 4, 'https://media-cms.vrbo.com//images/gxwgulxyxxy1/70kJsxr01x9klZh6E4oFdT/e454a9f9ee08b2b042000fd5c590ee9d/0_200419149-001.jpg?impolicy=resizecrop&rw=1024&rh=429&ch=429&cw=1024&ra=fill&q=mediumHigh', 2, 5),
    (026, '993 Saints Ave', 'Toronto, Ontario', 'Fairmont par Hotelstawadros', Array['647-899-0010'], 'uottawa@fairmont.ca', 3, 'https://phgcdn.com/images/uploads/YQBLC/masthead/1600x813-Exterior-2-Fairmont-le-Chateau-Montebello-Quebec-Canada.jpg', 2, 5),
    (027, '632 Cosmic Ave', 'Toronto, Ontario', 'King par Hotelstawadros', Array['647-746-4764'], 'uottawa@king.ca', 5, 'https://www.telegraph.co.uk/content/dam/Travel/hotels/2022/march/the-langdale-hotel-lake-district-p.jpg', 2, 5),
    (028, '604 Hunter Ave', 'Toronto, Ontario', 'Chelsea par Hotelstawadros', Array['647-904-2211'], 'uottawa@chelsea.ca', 3, 'https://media-cdn.tripadvisor.com/media/photo-s/18/2a/3b/f8/in-the-middle-of-the.jpg', 2, 5), 
	(031, '989 Fountain St', 'Montreal, Quebec', 'Hilton par Hotelsguad', Array['418-444-1111'], 'uottawa@hilton.ca', 4, 'https://images.charmingsardinia.com/hotels/1077/static/files/bio-hotel-hermitage01.jpg', 3, 5),
    (032, '554 Middle Ave', 'Montreal, Quebec', 'Universel par Hotelsguad', Array['418-222-7575'], 'uottawa@universel.ca', 4, 'https://www.fodors.com/wp-content/uploads/2017/10/mnt8.jpg', 3, 5),
    (033, '713 Oval St', ', Montreal, Quebec', 'Lofts par Hotelsguad', Array['418-783-3972'], 'uottawa@lofts.ca', 4, 'https://www.planetware.com/wpimages/2019/04/canada-quebec-quebec-city-best-hotels-auberge-saint-antoine.jpg', 3, 5),
    (034, '934 Bacon Rd', 'Montreal, Quebec', 'Concorde par Hotelsguad', Array['418-082-5126'], 'uottawa@concorde.ca', 5, 'https://www.gouverneur.com/uploads/1/0/6/8/106825145/published/gouvernement-provincial-hiver_3.jpg?1576850606', 3, 5),
    (035, '712 Maple St', 'Montreal, Quebec', 'Jardin par Hotelsguad', Array['418-785-5000'], 'uottawa@jardin.ca', 4, 'https://media-cms.vrbo.com//images/gxwgulxyxxy1/70kJsxr01x9klZh6E4oFdT/e454a9f9ee08b2b042000fd5c590ee9d/0_200419149-001.jpg?impolicy=resizecrop&rw=1024&rh=429&ch=429&cw=1024&ra=fill&q=mediumHigh', 3, 5),
    (036, '521 Anchor Ave', 'Montreal, Quebec', 'Quartier par Hotelsguad', Array['418-899-0010'], 'uottawa@quartier.ca', 3, 'https://phgcdn.com/images/uploads/YQBLC/masthead/1600x813-Exterior-2-Fairmont-le-Chateau-Montebello-Quebec-Canada.jpg', 3, 5),
    (037, '549 Chestnut Ave', 'Montreal, Quebec', 'Travelodge par Hotelsguad', Array['418-746-4764'], 'uottawa@travelodge.ca', 2, 'https://www.telegraph.co.uk/content/dam/Travel/hotels/2022/march/the-langdale-hotel-lake-district-p.jpg', 3, 5),
    (038, '741 Arctic Ave', 'Montreal, Quebec', 'Repotel par Hotelsguad', Array['418-904-2211'], 'uottawa@repotel.ca', 5, 'https://media-cdn.tripadvisor.com/media/photo-s/18/2a/3b/f8/in-the-middle-of-the.jpg', 3, 5), 
	(041, '831 Draven St', 'Vancouver, British Columbia', 'Element par Hotelswave', Array['604-444-1111'], 'uottawa@element.ca', 4, 'https://upload.wikimedia.org/wikipedia/commons/a/a9/Hotel_vanc_2007.jpg', 4, 5),
	(042, '622 Knight Ave', 'Vancouver, British Columbia', 'Panpacif par Hotelswave', Array['604-222-7575'], 'uottawa@panpacif.ca', 2, 'https://www.traveller.com.au/content/dam/images/g/m/7/x/p/f/image.gallery.galleryLandscape.620x414.gmakjr.png/1453333612558.jpg', 4, 5),
	(043, '482 Petal St', 'Vancouver, British Columbia', 'Marpole par Hotelswave', Array['604-783-3972'], 'uottawa@marpole.ca', 4, 'https://content.r9cdn.net/rimg/himg/c4/a0/5e/ice-32483-102819633-191720.jpg?width=440&height=220&crop=true', 4, 5),
	(044, '903 Garnet Rd', 'Vancouver, British Columbia', 'Executive par Hotelswave', Array['604-082-5126'], 'uottawa@executive.ca', 4, 'https://storeys.com/wp-content/uploads/2023/03/Marcon-W-Pender-Richards-Street-Downtown-Vancouver-Hotel-1.jpg', 4, 5),
	(045, '510 Shorten St', 'Vancouver, British Columbia', 'Sutton par Hotelswave', Array['604-785-5000'], 'uottawa@sutton.ca', 5, 'https://cf.bstatic.com/xdata/images/hotel/270x200/88496364.jpg?k=fc4daae0b1c02c9e1177f67ec789ab88980155c598342fe8487291a791c590d8&o=', 4, 5),
	(046, '614 Kream Ave', 'Vancouver, British Columbia', 'River par Hotelswave', Array['604-899-0010'], 'uottawa@river.ca', 3, 'https://media-magazine.trivago.com/wp-content/uploads/2018/08/29080558/hotel-blu-vancouver.jpeg', 4, 5),
	(047, '741 Park Ave', 'Vancouver, British Columbia', 'Darius par Hotelswave', Array['604-746-4764'], 'uottawa@darius.ca', 5, 'https://media.hrs.com/media/image/05/3e/e1/Four_Seasons_Hotel_Vancouver-Vancouver-Aussenansicht-1-33285_1280x1280.jpg', 4, 5),
	(048, '852 Beaux Ave', 'Vancouver, British Columbia', 'Morgana par Hotelswave', Array['604-844-6667'], 'uottawa@morgana.ca', 3, 'https://ik.imgkit.net/3vlqs5axxjf/external/ik-seo/http://images.ntmllc.com/v4/hotel/P94/P94601/P94601_EXT_ZB34FD/910-Beach-Ave-Apartment-Hotel-Exterior.jpg?tr=w-780%2Ch-437%2Cfo-auto', 4, 5), 
	(051, '314 Riven St', 'Halifax, Nova Scotia', 'Malphite par Hotelswave', Array['902-543-1400'], 'uottawa@malphite.ca', 3, 'https://www.novascotia.com/sites/default/files/2019-05/Quarterdeck%20Resort%20Villas%201920x1080.jpg', 5, 5),
	(052, '105 Jade Ave', 'Halifax, Nova Scotia', 'Marriott par Hotelswave', Array['902-111-3995'], 'uottawa@marriott.ca', 4, 'https://cdn.budgetyourtrip.com/images/photos/headerphotos/medium/canada_halifax.jpg', 5, 5),
	(053, '639 Church St', 'Halifax, Nova Scotia', 'Mundo par Hotelswave', Array['902-888-9979'], 'uottawa@mundo.ca', 5, 'https://static.wixstatic.com/media/3aafcb_9f55001595ee4e22b63a0c6a3264edb8~mv2.jpg/v1/fill/w_640,h_426,al_l,q_80,usm_0.66_1.00_0.01,enc_auto/3aafcb_9f55001595ee4e22b63a0c6a3264edb8~mv2.jpg', 5, 5),
	(054, '834 Rose Rd', 'Halifax, Nova Scotia', 'Sigma par Hotelswave', Array['902-002-5146'], 'uottawa@sigma.ca', 3, 'https://i0.wp.com/files.tripstodiscover.com/files/2015/05/White-Point-Beach-Resort.jpg?resize=784%2C588', 5, 5),
	(055, '128 Trinity St', 'Halifax, Nova Scotia', 'Delta par Hotelswave', Array['902-178-4343'], 'uottawa@delta.ca', 5, 'https://www.whitepoint.com/content/uploads/2022/12/WhitePointBbeachResortatsunset-1920x898.jpg', 5, 5),
	(056, '843 Manor Ave', 'Halifax, Nova Scotia', 'Winston par Hotelswave', Array['902-624-1545'], 'uottawa@winston.ca', 4, 'https://content.r9cdn.net/himg/7a/39/4c/leonardo-31779-150589310-299499.jpg', 5, 5),
	(057, '731 Mount Ave', 'Halifax, Nova Scotia', 'McCree par Hotelswave', Array['902-746-4565'], 'uottawa@mccree.ca', 3, 'https://www.ca.kayak.com/rimg/himg/20/39/cb/leonardo-1053285-hotel_O-295650.jpg?width=1366&height=768&xhint=1320&yhint=829&crop=true', 5, 5),
	(058, '475 Silver Ave', 'Halifax, Nova Scotia', 'Lucio par Hotelswave', Array['902-355-8632'], 'uottawa@lucio.ca', 2, 'https://www.choicehotels.com/hotelmedia/CA/NS/halifax/CN207/320/CN207Exterior06_1.jpg', 5, 5);
	
	
INSERT INTO public.app_capacity(
    id, capacity)
    VALUES (1, 'Single'),
(2, 'Double'),
(3, 'Suite'); 



