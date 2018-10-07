#include <iostream>
#include <algorithm> // for copy
#include <iterator> // for ostream_iterator
#include <vector>
#include <igl/point_mesh_squared_distance.h>

namespace p2mesh {
void find_closest_point_on_mesh(
    const std::vector<float>& P, //Kx3, K query points
	const std::vector<float>& V, //Nx3, mesh vertices
	const std::vector<int>&   F, //Mx3, mesh face indices
	std::vector<float>& C, //Kx3, K closest points
	std::vector<int>&   I, //Kx1, corresponding mesh indices
	std::vector<float>& D  //Kx1, squared distances
)
{
    const int K = P.size()/3;
    const int N = V.size()/3;
    const int M = F.size()/3;

	Eigen::MatrixXf P_ = Eigen::MatrixXf::Map(&P[0], K, 3);
	Eigen::MatrixXf V_ = Eigen::MatrixXf::Map(&V[0], N, 3);
	Eigen::MatrixXi F_ = Eigen::MatrixXi::Map(&F[0], M, 3);
	Eigen::MatrixXf C_;
	Eigen::VectorXi I_;
	Eigen::VectorXf D_;

	igl::point_mesh_squared_distance(P_, V_, F_, D_, I_, C_);

    C.resize(C_.size());
    I.resize(I_.size());
    D.resize(D_.size());
    Eigen::MatrixXf::Map(&C[0], K, 3) = C_;
	Eigen::VectorXi::Map(&I[0], K, 1) = I_;
	Eigen::VectorXf::Map(&D[0], K, 1) = D_;
}
}//p2mesh