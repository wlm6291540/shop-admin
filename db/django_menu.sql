/*
 Navicat Premium Data Transfer

 Source Server         : 192.168.200.125
 Source Server Type    : MySQL
 Source Server Version : 50729
 Source Host           : 192.168.200.125:33060
 Source Schema         : shop_admin

 Target Server Type    : MySQL
 Target Server Version : 50729
 File Encoding         : 65001

 Date: 01/04/2020 16:34:22
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for django_menu
-- ----------------------------
DROP TABLE IF EXISTS `django_menu`;
CREATE TABLE `django_menu`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `desc` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `parent_id` int(11) NULL DEFAULT NULL,
  `url` varchar(63) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `icon` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `type` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `system_menu_parent_id_c715739f_fk_system_menu_id`(`parent_id`) USING BTREE,
  CONSTRAINT `system_menu_parent_id_c715739f_fk_system_menu_id` FOREIGN KEY (`parent_id`) REFERENCES `django_menu` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 52 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_menu
-- ----------------------------
INSERT INTO `django_menu` VALUES (1, '主页', '主页', NULL, '/main/view', 'layui-icon-home\r\n', 1);
INSERT INTO `django_menu` VALUES (2, '系统管理', '菜单', NULL, '/system/view', 'layui-icon-set', 1);
INSERT INTO `django_menu` VALUES (3, '控制台', NULL, 1, '/main/console/view', 'layui-icon-console\r\n', 1);
INSERT INTO `django_menu` VALUES (4, '菜单管理', '页面,菜单', 2, '/system/menu/view', NULL, 1);
INSERT INTO `django_menu` VALUES (5, '角色管理', NULL, 2, '/system/role/view', NULL, 1);
INSERT INTO `django_menu` VALUES (7, '用户管理', NULL, 2, '/system/user/view', NULL, 1);
INSERT INTO `django_menu` VALUES (8, '添加菜单', NULL, 4, '/system/menu/add', NULL, 2);
INSERT INTO `django_menu` VALUES (9, '删除菜单', NULL, 4, '/system/menu/delete', NULL, 2);
INSERT INTO `django_menu` VALUES (10, '更新菜单', NULL, 4, '/system/menu/update', NULL, 2);
INSERT INTO `django_menu` VALUES (11, '获取菜单列表', NULL, 4, '/system/menu/list', NULL, 2);
INSERT INTO `django_menu` VALUES (12, '商品管理', NULL, NULL, '/goods/view', 'layui-icon-app\r\n', 1);
INSERT INTO `django_menu` VALUES (13, '订单管理', NULL, NULL, '/order/view', 'layui-icon-template-1', 1);
INSERT INTO `django_menu` VALUES (14, '用户管理', NULL, NULL, '/user/view', 'layui-icon-username\r\n', 1);
INSERT INTO `django_menu` VALUES (15, '品牌管理', NULL, 12, '/goods/brand/view', NULL, 1);
INSERT INTO `django_menu` VALUES (16, '商品分类', NULL, 12, '/goods/category/view', NULL, 1);
INSERT INTO `django_menu` VALUES (17, '商品列表', NULL, 12, '/goods/list/view', NULL, 1);
INSERT INTO `django_menu` VALUES (18, '订单列表', NULL, 13, '/order/list/view', NULL, 1);
INSERT INTO `django_menu` VALUES (19, '用户列表', NULL, 14, '/user/list/view', NULL, 1);
INSERT INTO `django_menu` VALUES (20, '添加角色', NULL, 5, '/system/role/add', NULL, 2);
INSERT INTO `django_menu` VALUES (21, '删除角色', NULL, 5, '/system/role/delete', NULL, 2);
INSERT INTO `django_menu` VALUES (22, '修改角色', NULL, 5, '/system/role/update', NULL, 2);
INSERT INTO `django_menu` VALUES (23, '角色列表', NULL, 5, '/system/role/list', NULL, 2);
INSERT INTO `django_menu` VALUES (24, '添加用户', NULL, 7, '/system/user/add', NULL, 2);
INSERT INTO `django_menu` VALUES (25, '禁用/激活用户', NULL, 7, '/system/user/active', NULL, 2);
INSERT INTO `django_menu` VALUES (26, '角色-用户列表', NULL, 5, '/system/role/role_user', NULL, 2);
INSERT INTO `django_menu` VALUES (27, '角色-菜单列表', NULL, 5, '/system/role/role_menu', NULL, 2);
INSERT INTO `django_menu` VALUES (28, '角色用户绑定', NULL, 5, '/system/role/role_user/bind', NULL, 2);
INSERT INTO `django_menu` VALUES (29, '角色菜单绑定', NULL, 5, '/system/role/role_menu/bind', NULL, 2);
INSERT INTO `django_menu` VALUES (30, '菜单树', NULL, 4, '/system/menu/tree', NULL, 2);
INSERT INTO `django_menu` VALUES (31, '修改用户', NULL, 7, '/system/user/update', NULL, 2);
INSERT INTO `django_menu` VALUES (32, '用户列表', NULL, 7, '/system/user/list', NULL, 2);
INSERT INTO `django_menu` VALUES (33, '品牌列表', '分页', 15, '/goods/brand/list', NULL, 2);
INSERT INTO `django_menu` VALUES (34, '品牌列表', '所有品牌', 15, '/goods/brand/all_list', NULL, 2);
INSERT INTO `django_menu` VALUES (35, '添加品牌', NULL, 15, '/goods/brand/add', NULL, 2);
INSERT INTO `django_menu` VALUES (36, '修改品牌', NULL, 15, '/goods/brand/update', NULL, 2);
INSERT INTO `django_menu` VALUES (37, '删除品牌', NULL, 15, '/goods/brand/delete', NULL, 2);
INSERT INTO `django_menu` VALUES (38, '分类列表', NULL, 16, '/goods/category/list', NULL, 2);
INSERT INTO `django_menu` VALUES (39, '添加分类', NULL, 16, '/goods/category/add', NULL, 2);
INSERT INTO `django_menu` VALUES (40, '修改分类', NULL, 16, '/goods/category/update', NULL, 2);
INSERT INTO `django_menu` VALUES (41, '删除分类', NULL, 16, '/goods/category/delete', NULL, 2);
INSERT INTO `django_menu` VALUES (42, '分类树', NULL, 16, '/goods/category/tree', NULL, 2);
INSERT INTO `django_menu` VALUES (43, '一级分类', NULL, 16, '/goods/category/parent', NULL, 2);
INSERT INTO `django_menu` VALUES (44, '商品列表', NULL, 17, '/goods/list/list', NULL, 2);
INSERT INTO `django_menu` VALUES (45, '商品上下架', NULL, 17, '/goods/list/on_sale', NULL, 2);
INSERT INTO `django_menu` VALUES (46, '修改价格', NULL, 17, '/goods/list/price_update', NULL, 2);
INSERT INTO `django_menu` VALUES (47, '获取订单列表', NULL, 18, '/order/list/list', NULL, 2);
INSERT INTO `django_menu` VALUES (48, '获取用户列表', NULL, 19, '/user/list/list', NULL, 2);
INSERT INTO `django_menu` VALUES (49, '添加用户', NULL, 19, '/user/list/add', NULL, 2);
INSERT INTO `django_menu` VALUES (50, '修改用户', NULL, 19, '/user/list/update', NULL, 2);
INSERT INTO `django_menu` VALUES (51, '用户充值', NULL, 19, '/user/list/charge', NULL, 2);

SET FOREIGN_KEY_CHECKS = 1;
