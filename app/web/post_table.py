from app.web import web
from flask import render_template, request
import time
from models.base import db
from models.table import Basic_property, Dynamic_property, Geo_property, Tree_brand, \
    GE_analysis, GP_analysis, Fzbh_analysis, Stss_analysis, Qxkf_detect, Bch_analysis, Pic_record


# 添加古树基本属性表
@web.route('/add_basic_property', methods=["POST"])
def add_basic_property():
    data = eval(request.data)
    zw_name = data["zw_name"]
    ld_name = data["ld_name"]
    bm_name = data["bm_name"]
    family = data["family"]
    genus = data["genus"]
    province = data["province"]
    city = data["city"]
    area = data["area"]
    town = data["town"]
    village = data["village"]
    place_name = data["place_name"]
    palce = data["palce"]
    placing_character = data["placing_character"]
    owner = data["owner"]
    level = data["level"]
    character_code = data["character_code"]
    jd_record = data["jd_record"]
    gh_unit = data["gh_unit"]
    username = data["username"]
    is_signed = data["is_signed"]
    tree_code = data["tree_code"]
    basic_property = Basic_property(tree_code=tree_code, zw_name=zw_name, ld_name=ld_name, bm_name=bm_name,
                                    family=family, genus=genus,
                                    town=town, village=village,
                                    place_name=place_name, palce=palce, placing_character=placing_character,
                                    owner=owner, level=level, character_code=character_code, jd_record=jd_record,
                                    gh_unit=gh_unit, username=username, is_signed=is_signed)
    db.session.add(basic_property)
    db.session.commit()   # ok
    return 'commit success'


# 添加古树动态属性表
@web.route('/add_dynamic_property', methods=["POST"])
def add_dynamic_property():
    data = eval(request.data)
    print(data)
    investigate_id = data["investigate_id"]
    describe = data["describe"]
    reason = data["reason"]
    affect_factor = data["affect_factor"]
    height = data["height"]
    bust = data["bust"]
    c_average = data["c_average"]
    c_dx = data["c_dx"]
    c_nb = data["c_nb"]
    g_vigor = data["g_vigor"]
    g_environment = data["g_environment"]
    real_age = data["real_age"]
    estimate_age = data["estimate_age"]
    basis = data["basis"]
    history = data["history"]
    history_pic = data["history_pic"]
    conserve_status = ''.join(data["conserve_status"]) # !
    yhfz_status = ''.join(data["yhfz_status"])         # !
    username = data["username"]
    # investigate_time = data["investigate_time"]      # 时间格式待定
    tree_code = data["tree_code"]
    dynamic_property = Dynamic_property(investigate_id=investigate_id, describe=describe,
                                        reason=reason, affect_factor=affect_factor,
                                        height=height, bust=bust, c_average=c_average, c_dx=c_dx, c_nb=c_nb,
                                        g_vigor=g_vigor, g_environment=g_environment,
                                        real_age=real_age, estimate_age=estimate_age, basis=basis, history=history,
                                        history_pic=history_pic, conserve_status=conserve_status,
                                        yhfz_status=yhfz_status, username=username, tree_code=tree_code)
    db.session.add(dynamic_property)
    db.session.commit()   # ok
    return 'commit success'


# 添加古树地理属性表
@web.route('/add_geo_property', methods=["POST"])
def add_geo_property():
    data = eval(request.data)
    adcode = data["adcode"]
    longitude = data["longitude"]
    latitude = data["latitude"]
    elevation = data["elevation"]
    aspect = data["aspect"]
    slope = data["slope"]
    slope_position = data["slope_position"]
    tree_code = data["tree_code"]
    geo_property = Geo_property()
    # db.session.add(geo_property)
    # db.session.commit()  # ok
    return 'commit success'


# 添加古树图片记录
@web.route("/add_pic_record", methods=["POST"])
def add_pic_record():
    data = eval(request.data)
    path = data["path"]
    explain = data["explain"]
    update_time = data["update_time"]
    tree_code = data["tree_code"]
    using = True
    update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    pic_record = Pic_record(tree_code=tree_code, path=path, explain=explain, update_time=update_time, using=using)
    db.session.add(pic_record)
    db.session.commit()  # ok
    return 'commit success'


# 添加古树树牌信息
@web.route('/add_tree_brand', methods=["POST"])
def add_tree_brand():
    data = eval(request.data)
    has_brand = data["has_brand"]
    is_right = data["is_right"]
    content = data["content"]
    brand_right = data["brand_right"]
    brand_pic = data["brand_pic"]
    update_time = data["update_time"]
    tree_code = data["tree_code"]
    update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    tree_brand = Tree_brand(tree_code=tree_code, has_brand=has_brand, is_right=is_right, content=content,
                            brand_right=brand_right,
                            brand_pic=brand_pic, update_time=update_time)
    db.session.add(tree_brand)    # ok
    db.session.commit()
    return 'commit success'


# 生长环境评估分析
@web.route('/add_ge_analysis', methods=["POST"])
def add_ge_analysis():
    data = eval(request.data)
    elevation = data["elevation"]
    habitat_type = data["habitat_type"]
    plain_type = data["plain_type"]
    plain_type = ''.join(plain_type)
    highland_type = data["highland_type"]
    aspect = data["aspect"]
    slope = data["slope"]
    slope_position = data["slope_position"]
    is_pollution = data["is_pollution"]
    varia = data["varia"]
    soil_texture = data["soil_texture"]
    soil_capacity = data["soil_capacity"]
    organic_content = data["organic_content"]
    sample_result = data["sample_result"]

    hydrolyze_N = data["hydrolyze_N"]
    valid_P = data["valid_P"]
    rapid_K = data["rapid_K"]
    saltness = data["saltness"]
    ec_value = data["ec_value"]
    ph_value = data["ph_value"]

    is_buried = data["is_buried"]
    buried_depth = data["buried_depth"]
    root_water = data["root_water"]

    protect_E = data["protect_E"]
    protect_W = data["protect_W"]
    protect_S = data["protect_S"]
    protect_N = data["protect_N"]
    protect_pic = data["protect_pic"]
    other_plants = data["other_plants"]
    evaluation = data["evaluation"]
    envoriment_problem = data["envoriment_problem"]
    has_structures = data["has_structures"]
    structures_type = data["structures_type"]
    structures_affect = data["structures_affect"]
    nutrient_status = data["nutrient_status"]
    pic_path = data["pic_path"]
    update_time = data["update_time"]
    using = True
    tree_code = data["tree_code"]
    update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    ge_analysis = GE_analysis(tree_code=tree_code, elevation=elevation, habitat_type=habitat_type, plain_type=plain_type, highland_type=highland_type,
                              aspect=aspect, slope=slope, slope_position=slope_position, is_pollution=is_pollution, varia=varia, soil_texture=soil_texture,
                              soil_capacity=soil_capacity, organic_content=organic_content, sample_result=sample_result, hydrolyze_N=hydrolyze_N,
                              valid_P=valid_P, rapid_K=rapid_K, saltness=saltness, ec_value=ec_value, ph_value=ph_value, is_buried=is_buried, buried_depth=buried_depth,
                              root_water=root_water, protect_E=protect_E, protect_W=protect_W, protect_S=protect_S, protect_N=protect_N, protect_pic=protect_pic,
                              other_plants=other_plants, evaluation=evaluation, envoriment_problem=envoriment_problem, has_structures=has_structures, structures_type=structures_type,
                              structures_affect=structures_affect, nutrient_status=nutrient_status, pic_path=pic_path, update_time=update_time, using=using)
    db.session.add(ge_analysis)
    db.session.commit()   # ok
    return 'commit success'


# 生长势分析
@web.route('/add_gp_analysis', methods=["POST"])
def add_gp_analysis():
    data = eval(request.data)
    shoot_type = data["shoot_type"]
    shoot = data["shoot"]
    normal_blade_rate = data["normal_blade_rate"]
    blade_persistent = data["blade_persistent"]
    growth_vigor = data["growth_vigor"]
    chlorophyll = data["chlorophyll"]
    Fo = data["Fo"]
    Fm = data["Fm"]
    update_time = data["update_time"]
    update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    tree_code = data["tree_code"]
    gp_analysis = GP_analysis(shoot_type=shoot_type, normal_blade_rate=normal_blade_rate, blade_persistent=blade_persistent,
                              growth_vigor=growth_vigor, chlorophyll=chlorophyll, Fo=Fo, Fm=Fm, update_time=update_time, tree_code=tree_code)
    db.session.add(gp_analysis)
    db.session.commit()   # ok
    return 'commit success'


# 已采取复壮保护措施情况与分析
@web.route('/add_fzbh_analysis', methods=["POST"])
def add_fzbh_analysis():
    data = eval(request.data)
    protect = ''.join(data["protect"])
    soil_improve = ''.join(data["soil_improve"])
    is_block = data["is_block"]

    fit_status = data["fit_status"]
    drain_hole = data["drain_hole"]
    tech_level = data["tech_level"]
    outer = data["outer"]

    clean_status = data["clean_status"]
    antiseptic = data["antiseptic"]

    is_support = data["is_support"]
    hard_support = data["hard_support"]
    protaging = data["protaging"]
    steady = data["steady"]
    support_type = data["support_type"]
    support_isrea = data["support_isrea"]
    hoop_status = data["hoop_status"]
    rubber_is = data["rubber_is"]
    hoop_is = data["hoop_is"]

    has_ditch = data["has_ditch"]
    ditch_type = data["ditch_type"]
    ditch_num = data["ditch_num"]
    ditch_width = data["ditch_width"]
    ditch_length = data["ditch_length"]
    pipe_num = data["pipe_num"]
    matrix_constitute = data["matrix_constitute"]
    position_is = data["position_is"]
    capillary_roots = data["capillary_roots"]

    protect_eval = data["protect_eval"]
    pic = data["pic"]
    update_time = data["update_time"]
    update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    using = True
    tree_code = data["tree_code"]
    fzbh_analysis = Fzbh_analysis(protect=protect, soil_improve=soil_improve, is_block=is_block, fit_status=fit_status, drain_hole=drain_hole,
                                  tech_level=tech_level, outer=outer, clean_status=clean_status, antiseptic=antiseptic, is_support=is_support,
                                  hard_support=hard_support, protaging=protaging, steady=steady, support_type=support_type, support_isrea=support_isrea,
                                  hoop_status=hoop_status, rubber_is=rubber_is, hoop_is=hoop_is, has_ditch=has_ditch, ditch_type=ditch_type,
                                  ditch_num=ditch_num, ditch_width=ditch_width, ditch_length=ditch_length, pipe_num=pipe_num, matrix_constitute=matrix_constitute,
                                  position_is=position_is, capillary_roots=capillary_roots, protect_eval=protect_eval, pic=pic, update_time=update_time, using=using, tree_code=tree_code)
    db.session.add(fzbh_analysis)
    db.session.commit()   # ok
    return 'commit success'


# 树体损伤情况评估
@web.route('/add_stss_analysis', methods=["POST"])
def add_stss_analysis():
    data = eval(request.data)
    base1 = data["base1"]
    pic_base1 = data["pic_base1"]
    base2 = data["base2"]
    pic_base2 = data["pic_base2"]
    base3 = data["base3"]
    pic_base3 = data["pic_base3"]

    trunk1 = data["trunk1"]
    pic_trunk1 = data["pic_trunk1"]
    trunk2 = data["trunk2"]
    pic_trunk2 = data["pic_trunk2"]
    trunk3 = data["trunk3"]
    pic_trunk3 = data["pic_trunk3"]

    skeleton1 = data["skeleton1"]
    pic_ske1 = data["pic_ske1"]
    skeleton2 = data["skeleton2"]
    pic_ske2 = data["pic_ske2"]
    skeleton3 = data["skeleton3"]
    pic_ske3 = data["pic_ske3"]

    damage_status = data["damage_status"]
    update_time = data["update_time"]
    update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    stss_analysis = Stss_analysis(base1=base1, pic_base1=pic_base1, base2=base2, pic_base2=pic_base2, base3=base3, pic_base3=pic_base3,
                                  trunk1=trunk1, pic_trunk1=pic_trunk1, trunk2=trunk2, pic_trunk2=pic_trunk2, trunk3=trunk3, pic_trunk3=pic_trunk3,
                                  skeleton1=skeleton1, pic_ske1=pic_ske1, skeleton2=skeleton2, pic_ske2=pic_ske2, skeleton3=skeleton3, pic_ske3=pic_ske3,
                                  damage_status=damage_status, update_time=update_time)
    db.session.add(stss_analysis)
    db.session.commit()   # ok
    return 'commit success'


# 树体倾斜、空腐情况检测
@web.route('/add_qxkf_detect', methods=["POST"])
def add_qxkf_detect():
    data = eval(request.data)
    base_loose = data["base_loose"]
    pic_1 = data["pic_1"]
    root_rot = data["root_rot"]
    pic_2 = data["pic_2"]
    root_bare = data["root_bare"]
    bare_length = data["bare_length"]
    pic_3 = data["pic_3"]
    has_absound = data["has_absound"]
    trunk_inclined = data["trunk_inclined"]
    pic_4 = data["pic_4"]
    has_abbranch = data["has_abbranch"]
    pic_5 = data["pic_5"]
    lopsided = data["lopsided"]
    pic_6 = data["pic_6"]
    deadwood = data["deadwood"]
    pic_7 = data["pic_7"]
    twig = data["twig"]
    pic_8 = data["pic_8"]
    empty_rot_rate = data["empty_rot_rate"]
    qxkf_eval = data["qxkf_eval"]
    update_time = data["update_time"]
    update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    qxkf_detect = Qxkf_detect(base_loose=base_loose, pic_1=pic_1, root_rot=root_rot, pic_2=pic_2, root_bare=root_bare,
                              bare_length=bare_length, pic_3=pic_3, has_absound=has_absound, trunk_inclined=trunk_inclined,
                              pic_4=pic_4, has_abbranch=has_abbranch, pic_5=pic_5, lopsided=lopsided, pic_6=pic_6,
                              deadwood=deadwood, pic_7=pic_7, twig=twig, pic_8=pic_8, empty_rot_rate=empty_rot_rate,
                              qxkf_eval=qxkf_eval, update_time=update_time)
    db.session.add(qxkf_detect)   # ok
    db.session.commit()
    return 'commit success'


# 病虫害分析
@web.route('/add_bch_analysis', methods=["POST"])
def add_bch_analysis():
    data = eval(request.data)
    bmoth_status = data["bmoth_status"]
    bmoth_name = data["bmoth_name"]
    bdisease_status = data["bdisease_status"]
    bdisease_name = data["bdisease_name"]
    base_pic = data["base_pic"]

    tmoth_status = data["tmoth_status"]
    tmoth_name = data["tmoth_name"]
    tdisease_status = data["tdisease_status"]
    tdisease_name = data["tdisease_name"]
    trunk_pic = data["trunk_pic"]

    smoth_status = data["smoth_status"]
    smoth_name = data["smoth_name"]
    sdisease_status = data["sdisease_status"]
    sdisease_name = data["sdisease_name"]
    ske_pic = data["ske_pic"]

    blade_status = data["blade_status"]
    blade_name = data["blade_name"]
    blade_pic = data["blade_pic"]

    branch_status = data["branch_status"]
    branch_name = data["branch_name"]
    branch_pic = data["branch_pic"]

    total_eval = data["total_eval"]
    update_time = data["update_time"]
    update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    bch_analysis = Bch_analysis(bmoth_status=bmoth_status, bmoth_name=bmoth_name, bdisease_status=bdisease_status, bdisease_name=bdisease_name, base_pic=base_pic,
                                tmoth_status=tmoth_status, tmoth_name=tmoth_name, tdisease_status=tdisease_status, tdisease_name=tdisease_name, trunk_pic=trunk_pic,
                                smoth_status=smoth_status, smoth_name=smoth_name, sdisease_status=sdisease_status, sdisease_name=sdisease_name, ske_pic=ske_pic,
                                blade_status=blade_status, blade_name=blade_name, blade_pic=blade_pic, branch_status=branch_status, branch_name=branch_name,
                                branch_pic=branch_pic, total_eval=total_eval, update_time=update_time)
    db.session.add(bch_analysis)
    db.session.commit()
    return 'commit success'
