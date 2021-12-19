function setStatioResult(result) {
	if (result.Fault.length) {
		$(".fault-panel").show();
		setResultFault(result);
	} else {
		$(".fault-panel").hide();
	}
	setResultNormal(result);
	setResultMeter(result);
	setResultTank(result);
	setResultInwater(result);
	setResultHeatPump(result);
	setResultElectric(result);
	setResultBackwater(result);
	setResultPressurePump(result);
	setResultSolar(result);
}

function getTrendIcon(val) {
	if (val > 0) return " <i class='fa fa-long-arrow-up text-danger' title='上升趋势'></i>";
	if (val < 0) return " <i class='fa fa-long-arrow-down text-info' title='下降趋势'></i>";
	return "";
}

function setResultFault(result) {
	$(".fault-list").html("");
	if (result.FaultEquipment.length) {
		$.each(result.FaultEquipment, function(idx, txt) {
			$(".fault-list").append('<span class="label label-danger">' + txt + '</span> ');
		});
	}
	if (result.FaultSensor.length) {
		$.each(result.FaultSensor, function(idx, txt) {
			$(".fault-list").append('<span class="label label-danger">' + txt + '</span> ');
		});
	}
}

function setResultNormal(result) {
	$(".value-work-status").html(result.Online ? "在线" : "离线");
	if (result.Remote == 1) {
		$(".value-work-mode").html("自动");
	} else if (result.Remote == 2) {
		$(".value-work-mode").html("手动");
	} else {
		$(".value-work-mode").html("未知");
	}
	$(".value-outside-temperature").html(result.AT + "℃");	

	if (result.TankCount == 2) {
		$(".value-mix-temperature").html(result.TankMixTemperature);
	}
}

function setResultMeter(result) {
	if (result.Ammeter >= 0) {
		$(".value-ammeter").html(result.Ammeter + "度");
	} else {
		$(".value-ammeter").html("X");
	}
	if (result.Watermeter >= 0) {
		$(".value-watermeter").html(result.Watermeter + "吨");
	} else {
		$(".value-watermeter").html("X");
	}
	if (result.AH >= 0) {
		$(".value-outside-hygronom").html(result.AH + "%");
	} else {
		$(".value-outside-hygronom").html("X");
	}
	if (result.WD >= 0) {
		$(".value-outside-anemoscope").html(result.WD + "米/秒");
	} else {
		$(".value-outside-anemoscope").html("X");
	}
}

function setResultTank(result) {
	if (result.TankCount == 1) {
		if (result.Tank[0].WT !== null) {
			var value = result.Tank[0].WT + "℃ " + getTrendIcon(result.Tank[0].LWT);
		} else {
			var value = '-- '
		}
		$('.value-tank').find('.wt').html(value);
		$('.value-tank-wt').html(value);

		if (result.Tank[0].WL !== null) {
			var value = result.Tank[0].WL + "米 " + getTrendIcon(result.Tank[0].LWL);
		} else {
			var value = "-- ";
		}
		$('.value-tank').find('.wl').html(value);
		$('.value-tank-wl').html(value);

		if (result.Tank[0].WP !== null) {
			var value = result.Tank[0].WP + "吨 ";
		} else {
			var value = "-- ";
		}
		$('.value-tank').find('.wp').html(value);
		$('.value-tank-wp').html(value);
	}

	if (result.TankCount == 2) {
		$.each(result.Tank,function(i, val) {
			if (result.Tank[i].WT !== null) {
				var value = result.Tank[i].WT + "℃ " + getTrendIcon(result.Tank[i].LWT);
			} else {
				var value = '-- ';
			}
			$('.value-tank-'+i).find('.wt').html(value);
			$('.value-tank-'+i+'-wt').html(value);

			if (result.Tank[i].WL !== null) {
				var value = result.Tank[i].WL + "米 " + getTrendIcon(result.Tank[i].LWL);
			} else {
				var value = '-- ';
			}
			$('.value-tank-'+i).find('.wl').html(value);
			$('.value-tank-'+i+'-wl').html(value);
			
			if (result.Tank[i].WP !== null) {
				var value = result.Tank[i].WP + "吨 ";
			} else {
				var value = '-- ';
			}
			$('.value-tank-'+i).find('.wp').html(value);
			$('.value-tank-'+i+'-wp').html(value);
		});
	}
}

function setResultInwater(result) {
	if (result.TankCount == 1) {
		if (result.InWater.F) {
			$('.M-Tank0InWater').find('.item-value-status').html('故障').addClass("state-fault").removeClass("state-ok");
			$('.inWater0').find(".switch").hide();
			$('.inWater0').find(".failed").show();
		} else if (result.InWater.S) {
			$('.M-Tank0InWater').find('.item-value-status').html('开启').removeClass('state-fault').addClass("state-ok");
			$('.inWater0').find(".switch").addClass('ok').show();
			$('.inWater0').find(".failed").hide();
		} else {
			$('.M-Tank0InWater').find('.item-value-status').html('关闭').removeClass('state-ok').removeClass('state-fault');
			$('.inWater0').find(".switch").removeClass('ok').addClass('closed').show();
			$('.inWater0').find(".failed").hide();
		}
	}

	if (result.TankCount == 2) {
		$.each(result.InWater, function(i, val) {
			if (val.F) {
				$('.M-Tank'+i+'InWater').find('.item-value-status').html('故障').addClass("state-fault").removeClass("state-ok");
				$('.inWater'+i).find(".switch").hide();
				$('.inWater'+i).find(".failed").show();
			} else if (val.S) {
				$('.M-Tank'+i+'InWater').find('.item-value-status').html('开启').removeClass('state-fault').addClass("state-ok");
				$('.inWater'+i).find(".switch").addClass('ok').show();
				$('.inWater'+i).find(".failed").hide();
			} else {
				$('.M-Tank'+i+'InWater').find('.item-value-status').html('关闭').removeClass('state-ok').removeClass('state-fault');
				$('.inWater'+i).find(".switch").removeClass('ok').addClass('closed').show();
				$('.inWater'+i).find(".failed").hide();
			}
		});
	}
}

function setResultHeatPump(result) {
	if ((result.Mode & 1) && result.TankCount == 1) {
		$.each(result.Heatpump, function(idx, item) {
			if (item.V) {
				$('.M-Heatpump' + idx).show();
				if (item.S) {
					$(".HeatpumpItem" + idx).html("开启").removeClass("state-fault").addClass("state-ok");
					$('.M-Heatpump' + idx + '-State').html('开启').removeClass('state-fault').addClass("state-ok");
				} else if (item.F) {
					$(".HeatpumpItem" + idx).html("故障").addClass("state-fault").removeClass("state-ok");
					$('.M-Heatpump' + idx + '-State').html('故障').addClass('state-fault').removeClass("state-ok");
				} else if (item.C) {
					$(".HeatpumpItem" + idx).html("等待").removeClass("state-fault state-ok");
					$('.M-Heatpump' + idx + '-State').html('等待').removeClass("state-fault state-ok");
				} else {
					$(".HeatpumpItem" + idx).html("关闭").removeClass("state-fault state-ok");
					$('.M-Heatpump' + idx + '-State').html('关闭').removeClass("state-fault state-ok");
				}
			} else {
				$(".HeatpumpItem" + idx).html("　　").removeClass("state-fault state-ok");
				$('.M-Heatpump' + idx).hide();
			}
		});
	}

	if ((result.Mode & 1) && result.TankCount == 2) {
		$.each(result.Heatpump, function(idx, heatpump) {
			$.each(heatpump, function(jdx, item) {
				if (item.V) {
					$('.M-Heatpump' + idx + '-' + jdx).show();
					if (item.S) {
						$(".HeatpumpItem" + idx + '-' + jdx).html('开启').removeClass("state-fault").addClass("state-ok");
						$('.M-Heatpump' + idx + '-' + jdx + '-State').html('开启').removeClass('state-fault').addClass("state-ok");
					} else if (item.F) {
						$(".HeatpumpItem" + idx + '-' + jdx).html("故障").addClass("state-fault").removeClass("state-ok");
						$('.M-Heatpump' + idx + '-' + jdx + '-State').html('故障').addClass('state-fault').removeClass("state-ok");
					} else if (item.C) {
						$(".HeatpumpItem" + idx + '-' + jdx).html("等待").removeClass("state-fault state-ok");
						$('.M-Heatpump' + idx + '-' + jdx + '-State').html('等待').removeClass("state-fault state-ok");
					} else {
						$(".HeatpumpItem" + idx + '-' + jdx).html('关闭').removeClass("state-fault state-ok");
						$('.M-Heatpump' + idx + '-' + jdx + '-State').html('关闭').removeClass("state-fault state-ok");
					}
				} else {
					$(".HeatpumpItem" + idx + '-' + jdx).html("　　").removeClass("state-fault state-ok");
					$('.M-Heatpump'+idx+'-'+jdx).hide();
				}
			});
		});
	}
}

function setResultElectric(result) {
	$.each(result.EA, function(idx, EA) {
		if (EA.V) {
			$('.M-EA'+idx).show();
			if (EA.S) {
				$('.M-EA'+idx).find('.item-value-status').html('开启').removeClass('state-fault').addClass("state-ok");
				$('.electric'+idx).find(".off,.failed").hide();
				$('.electric'+idx).find(".on").show();
			} else {
				$('.M-EA'+idx).find('.item-value-status').html('关闭').removeClass("state-fault state-ok");
				$('.electric'+idx).find(".on,.failed").hide();
				$('.electric'+idx).find(".off").show();
			}
			if (EA.F) {
				$('.M-EA'+idx).find('.item-value-status').html('故障').addClass("state-fault").removeClass("state-ok");
				$('.electric'+idx).find(".on,.off").hide();
				$('.electric'+idx).find(".failed").show();
			}
		} else {
			$('.M-EA'+idx).hide();
			$('.electric'+idx).find(".on,.off,.failed").hide();
		}
	});
}

function setResultBackwater(result) {
	if(result.BackWater.V){
		$('.M-Backwater').show();
		if(result.BackWater.F){
			$('.M-Backwater').find('.item-value-status').html('故障').addClass("state-fault").removeClass("state-ok");
			$('.Backwater-Panel').find(".failed").show();
			$('.Backwater-Panel').find(".switch,.switch").hide();
		} else {
			$('.Backwater-Panel').find(".switch").show();
			$('.Backwater-Panel').find(".failed").hide();
			if (result.BackWater.S) {
				$('.M-Backwater').find('.item-value-status').html('开启').removeClass('state-fault').addClass("state-ok");
				$('.Backwater-Panel').find(".switch").addClass('ok');
			} else {
				$('.M-Backwater').find('.item-value-status').html('关闭').removeClass("state-fault state-ok");
				$('.Backwater-Panel').find(".switch").removeClass('ok');
			}
		}
	} else {
		$('.Backwater-Panel').find(".invalid").show();
		$('.Backwater-Panel').find(".switch,.failed").hide();
		$('.M-Backwater').hide();
	}
	$('.Backwater-Value').html(result.BackWater.WT + "℃");
}

function setResultPressurePump(result) {
	$.each(result.PP, function(i, val) {
		$('.pp'+i).find('img').hide();
		if (val.V) {
			$('.M-PP'+i).show();
			if (val.F) {
				$('.M-PP'+i).find('.item-value-status').html('故障').addClass("state-fault").removeClass("state-ok");
				$('.pp'+i).find('.failed').show();
			} else {
				$('.M-PP'+i).find('.item-value-status').html('正常');
				if (val.S) {
					$('.M-PP'+i).find('.item-value-status').html('开启').removeClass('state-fault').addClass("state-ok");
					$('.pp'+i).find(".switch").removeClass('closed').addClass('ok').show();
				} else {
					$('.M-PP'+i).find('.item-value-status').html('关闭').removeClass("state-fault state-ok");
					$('.pp'+i).find(".switch").removeClass('ok').addClass('closed').show();
				}
			}
		} else {
			$('.M-PP'+i).hide();
			$('.pp'+i).find('.invalid').show();
		}
	});
}

function setResultSolar(result) {
	if (result.Mode & 2) {
		$.each(result.Solar, function(idx, solar) {
			if (solar.V) {
				$(".M-SolarItem" + idx).show();
				if (solar.F) {
					$(".SolarItem" + idx).html("故障").addClass("state-fault").removeClass("state-ok");
					$(".M-SolarItem" + idx + '-State').html("故障").addClass("state-fault").removeClass("state-ok");
				} else {
					if (solar.S) {
						$(".SolarItem" + idx).html(solar.T+"℃").addClass("state-ok").removeClass("state-fault");
						$(".M-SolarItem" + idx + '-State').html(solar.T + "℃").addClass("state-ok").removeClass("state-fault");
					} else {
						$(".SolarItem" + idx).html(solar.T+"℃").removeClass("state-ok").removeClass("state-fault");
						$(".M-SolarItem" + idx + '-State').html(solar.T + "℃").removeClass("state-ok").removeClass("state-fault");
					}
				}
			} else {
				$(".SolarItem" + idx).html("　　").removeClass("state-fault state-ok");
				$(".M-SolarItem" + idx).hide();
			}
		});
	}
}