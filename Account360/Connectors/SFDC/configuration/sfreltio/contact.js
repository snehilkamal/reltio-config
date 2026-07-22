var require = require.main.require.bind(require.main);
var reqlib = require('app-root-path').require;

var Q = require('q');
var log = reqlib('./lib/log');
var mapper = reqlib('./lib/mapper');
var utils = reqlib('./lib/utils');
var _ = require('lodash');
var mdm = reqlib('./lib/reltiomdm');
var tls = reqlib('./lib/tls');

var contact = {

    preProcess  : function(obj){
        try {
            if (obj.__entity) {
                var entity = obj.__entity;
                var entityObj = obj.__entityso;
                if (!entityObj) {
                    var em = mapper.getEntityMapping(tls.getCurrentTenant(), entity.type);
                    entityObj = mapper.convertFromMapping(entity, em);
                }
                utils.copyMissingAttributes(obj, entityObj);
            }

        } catch(e) {
            console.log('Error is'+e);
        }

    },

    postProcess : function(data, sfmapping) {

        var d = Q.defer();
        try {
            var result = false;
            if(sfmapping.custSpecificId && utils.isDefined(data[sfmapping.custSpecificId])) {
                result = mapper.convertaccountsf(tls.getCurrentTenant(), 'AccountJazz', sfmapping.recordType, false, data );
                var query = {
                    options: 'partialOverride'
                };
                mdm.create([result], query, function (res) {
                    log.info('Post tenant Specific completed ');
                    d.resolve();
                }, function (err) {
                    d.resolve();
                    log.info(err);
                });
            } else {
                d.resolve();
            }
        } catch(e) {
            d.resolve();
            log.info(e);

        } finally {
            return d.promise;
        }


    }
}

module.exports = contact;


