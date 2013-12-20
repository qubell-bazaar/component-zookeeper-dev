# utility 'patch' is not included in build-essentials cookbook
# so we need instal it in this way

p = package "patch" do
  action :install
end
p.run_action(:install)

include_recipe "zookeeper"
