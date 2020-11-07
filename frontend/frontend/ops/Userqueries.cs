using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace frontend.ops
{
    public class Userqueries
    {
        public string allNetworkcredentials = @"
                    query{
                        allNetworkcredentials{
                        edges{
                            node{
                            id
                            socialNetwork,
                            username,
                            email,
                            link,
                            password
                            password
                            }
                        }
                        }
                    }
                    ";
    }
}
