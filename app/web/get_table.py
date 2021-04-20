from app.web import web
from flask import render_template, request, jsonify
import time
from models.base import db
from models.table import Basic_property, Dynamic_property, Geo_property, Tree_brand, \
    GE_analysis, GP_analysis, Fzbh_analysis, Stss_analysis, Qxkf_detect, Bch_analysis, Pic_record


@web.route("/get_trees_info")
def get_trees_info():
    # 查询结果集合
    res = []
    basic_trees = Basic_property.query.all()
    for tree in basic_trees:
        # 每棵树的不同属性集合
        tree_info = {tree.tree_code: []}
        # 基础属性
        basic_property = {"basic_property": []}
        basic_property["basic_property"].append(
            {"id": tree.id, "tree_code": tree.tree_code, "zw_name": tree.zw_name, "ld_name": tree.ld_name,
             "bm_name": tree.bm_name, "family": tree.family, "genus": tree.genus, "town": tree.town,
             "village": tree.village,
             "place_name": tree.place_name, "palce": tree.placing_character, "owner": tree.owner, "level": tree.level,
             "character_code": tree.character_code, "jd_record": tree.jd_record, "gh_unit": tree.gh_unit,
             "username": tree.username,
             "is_signed": tree.is_signed, "using": tree.using})

        tree_info[tree.tree_code].append(basic_property)
        res.append(tree_info)

        # 动态属性
        dp = Dynamic_property.query.filter_by(tree_code=tree.tree_code).first()
        dynamic_property = {"dynamic_property": []}
        dynamic_property["dynamic_property"].append(
            {"id": dp.id, "describe": dp.describe, "reason": dp.reason, "affect_factor": dp.affect_factor,
             "height": dp.height, "bust": dp.bust, "c_average": dp.c_average, "c_dx": dp.c_dx, "c_nb": dp.c_nb,
             "g_vigor": dp.g_vigor, "g_environment": dp.g_environment, "real_age": dp.real_age,
             "estimate_age": dp.estimate_age, "basis": dp.basis, "history": dp.history, "history_pic": dp.history_pic,
             "conserve_status": dp.conserve_status, "yhfz_status": dp.yhfz_status, "investigate_id": dp.investigate_id,
             "using": dp.using, "tree_code": dp.tree_code})
        tree_info[tree.tree_code].append(dynamic_property)

        # 地理属性
        geo_p = Geo_property.query.filter_by(tree_code=tree.tree_code).first()
        geo_property = {"geo_property": []}
        geo_property["geo_property"].append(
            {"dt_id": geo_p.dt_id, "adcode": geo_p.adcode, "longitude": geo_p.longitude, "latitude": geo_p.latitude,
             "elevation": geo_p.elevation, "aspect": geo_p.aspect, "slope": geo_p.slope,
             "slope_position": geo_p.slope_position,
             "using": geo_p.using, "tree_code": geo_p.tree_code})
        tree_info[tree.tree_code].append(geo_property)

        # 图片记录
        pics = Pic_record.query.filter_by(tree_code=tree.tree_code).order_by("update_time").all()
        pic = pics[len(pics) - 1]
        pic_record = {"pic_record": []}
        pic_record["pic_record"].append(
            {"pic_id": pic.pic_id, "path": pic.path, "explain": pic.explain, "update_time": pic.update_time,
             "using": pic.using, "tree_code": pic.tree_code})
        tree_info[tree.tree_code].append(pic_record)

        # 树牌记录
        brands = Tree_brand.query.filter_by(tree_code=tree.tree_code).order_by("update_time").all()
        brand = brands[len(brands)-1]
        tree_brand = {"tree_brand": []}
        tree_brand["tree_brand"].append({"id": brand.id, "has_brand": brand.has_brand, "is_right": brand.is_right, "brand_pic": brand.brand_pic,
                                         "update_time": brand.update_time, "using": brand.using, "tree_code": brand.tree_code})
        tree_info[tree.tree_code].append(tree_brand)
    return jsonify(res)


@web.route("/get_tree_info/<tree_code>/")
def get_tree_info(tree_code):
    res = []
    # 基础属性
    tree = Basic_property.query.filter_by(tree_code=tree_code).first()
    basic_property = {"basic_property": []}
    basic_property["basic_property"].append(
        {"id": tree.id, "tree_code": tree.tree_code, "zw_name": tree.zw_name, "ld_name": tree.ld_name,
         "bm_name": tree.bm_name, "family": tree.family, "genus": tree.genus, "town": tree.town,
         "village": tree.village,
         "place_name": tree.place_name, "palce": tree.placing_character, "owner": tree.owner, "level": tree.level,
         "character_code": tree.character_code, "jd_record": tree.jd_record, "gh_unit": tree.gh_unit,
         "username": tree.username,
         "is_signed": tree.is_signed, "using": tree.using})
    res.append(basic_property)
    # 动态属性
    dp = Dynamic_property.query.filter_by(tree_code=tree_code).first()
    dynamic_property = {"dynamic_property": []}
    dynamic_property["dynamic_property"].append(
        {"id": dp.id, "describe": dp.describe, "reason": dp.reason, "affect_factor": dp.affect_factor,
         "height": dp.height, "bust": dp.bust, "c_average": dp.c_average, "c_dx": dp.c_dx, "c_nb": dp.c_nb,
         "g_vigor": dp.g_vigor, "g_environment": dp.g_environment, "real_age": dp.real_age,
         "estimate_age": dp.estimate_age, "basis": dp.basis, "history": dp.history, "history_pic": dp.history_pic,
         "conserve_status": dp.conserve_status, "yhfz_status": dp.yhfz_status, "investigate_id": dp.investigate_id,
         "using": dp.using, "tree_code": dp.tree_code})
    res.append(dynamic_property)
    geo_p = Geo_property.query.filter_by(tree_code=tree_code).first()
    geo_property = {"geo_property": []}
    geo_property["geo_property"].append(
        {"dt_id": geo_p.dt_id, "adcode": geo_p.adcode, "longitude": geo_p.longitude, "latitude": geo_p.latitude,
         "elevation": geo_p.elevation, "aspect": geo_p.aspect, "slope": geo_p.slope,
         "slope_position": geo_p.slope_position,
         "using": geo_p.using, "tree_code": geo_p.tree_code})
    res.append(geo_property)
    pics = Pic_record.query.filter_by(tree_code=tree_code).order_by("update_time").all()
    pic = pics[len(pics) - 1]
    pic_record = {"pic_record": []}
    pic_record["pic_record"].append(
        {"pic_id": pic.pic_id, "path": pic.path, "explain": pic.explain, "update_time": pic.update_time,
         "using": pic.using, "tree_code": pic.tree_code})
    res.append(pic_record)
    brands = Tree_brand.query.filter_by(tree_code=tree_code).order_by("update_time").all()
    brand = brands[len(brands) - 1]
    tree_brand = {"tree_brand": []}
    tree_brand["tree_brand"].append(
        {"id": brand.id, "has_brand": brand.has_brand, "is_right": brand.is_right, "brand_pic": brand.brand_pic,
         "update_time": brand.update_time, "using": brand.using, "tree_code": brand.tree_code})
    res.append(tree_brand)
    return jsonify(res)